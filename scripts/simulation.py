import numpy as np
from math import pi


class Simulation:
    def __init__(self, step_sim, init_pos, init_point, init_traj=None):
        # Constantes do modelo
        self.m = 0.25  # massa
        self.g = 9.81  # aceleração da gravidade
        self.l = 0.1  # tamanho
        self.kf = 1.744e-08  # constante de força
        self.Iz = 2e-4  # momento de inércia
        self.tau = 0.005
        self.Fg = np.array([[0], [-self.m * self.g]])

        # Parâmetros de simulação
        self.step_ratio = 10.0
        self.step_sim = step_sim  # Passo da simulação (C)
        self.step_control = step_sim * self.step_ratio  # Intervalo de amostragem
        self.t_sim = 0
        self.t_control = 0
        self.k = 0

        # Vetor de estados
        self.x = np.array([0.0, 0.0, init_pos[0], init_pos[1], 0.0, 0.0, 0.0, 0.0])

        # Comando de controle
        self.u = np.zeros(2)

        # Restrições do controle
        self.phi_max = 15 * np.pi / 180.0  # ângulo máximo
        self.w_max = 15000
        self.Fc_max = self.kf * self.w_max ** 2  # força de controle máxima
        self.Tc_max = self.l * self.kf * self.w_max ** 2

        # Controle das posições
        if init_point:
            self.ref_ = [init_point]
        else:
            self.ref_ = init_traj

        self.ref_ID = 0
        self.ref_IDN = len(self.ref_) - 1

    def iterate(self):
        if (self.k % self.step_ratio) == 0:
            # Extrai os dados do vetor
            ref_k = self.x[2:4]
            v_k = self.x[4:6]
            phi_k = self.x[6]
            ome_k = self.x[7]

            # Controle de posição
            kpP = np.array([0.075])
            kdP = np.array([0.25])

            eP = self.ref_[self.ref_ID] - ref_k
            eV = np.array([0.0, 0.0]) - v_k

            # Definição da próxima posição
            if np.linalg.norm(eP) < 0.1 and self.ref_ID < self.ref_IDN:
                print(f"Position {self.ref_ID} reached: {self.ref_[self.ref_ID]}")
                self.ref_ID += 1

            Fx = kpP * eP[0] + kdP * eV[0]
            Fy = kpP * eP[1] + kdP * eV[1] - self.Fg[1]
            Fy = np.maximum(0.2 * self.Fc_max, np.minimum(Fy, 0.8 * self.Fc_max))

            # Controle de atitude (ângulo phi)
            phi_ = np.arctan2(-Fx, Fy)

            if np.abs(phi_) > self.phi_max:
                signal = phi_ / np.absolute(phi_)
                phi_ = signal * self.phi_max
                # Limitando o ângulo
                Fx = Fy * np.tan(phi_)

            Fxy = np.array([Fx, Fy])
            Fc = np.linalg.norm(Fxy)
            f12 = np.array([Fc / 2.0, Fc / 2.0])

            kpA = np.array([0.75])
            kdA = np.array([0.05])

            ePhi = phi_ - phi_k
            eOme = 0.0 - ome_k

            Tc = kpA * ePhi + kdA * eOme
            Tc = np.maximum(-0.4 * self.Tc_max, np.minimum(Tc, 0.4 * self.Tc_max))

            # Delta de forças
            df12 = np.absolute(Tc) / 2.0
            if Tc >= 0.0:
                f12[0] = f12[0] + df12
                f12[1] = f12[1] - df12
            else:
                f12[0] = f12[0] - df12
                f12[1] = f12[1] + df12

            # Limitadores
            w1_ = np.sqrt(f12[0] / (self.kf))
            w2_ = np.sqrt(f12[1] / (self.kf))

            # Limitando o comando do motor
            w1 = np.maximum(0.0, np.minimum(w1_, self.w_max))
            w2 = np.maximum(0.0, np.minimum(w2_, self.w_max))

            # Determinação do comando de entrada
            self.u = np.array([w1, w2])

        # Simulação de um passo a frente
        self.x = self.__rk4(self.t_sim, self.step_sim, np.array(self.x), self.u)

        self.t_sim += self.step_sim
        self.t_control += self.step_control

        self.k += 1

        return self.x[2:4], self.x[6]

    def set_pos_x(self, pos_x):
        self.ref_[self.ref_ID][0] = pos_x
        print(self.ref_[self.ref_ID])

    def set_pos_y(self, pos_y):
        self.ref_[self.ref_ID][1] = pos_y
        print(self.ref_[self.ref_ID])

    def get_pos_x(self):
        return self.ref_[self.ref_ID][0]

    def get_pos_y(self):
        return self.ref_[self.ref_ID][1]

    def __rk4(self, tk, h, xk, uk):
        k1 = self.__x_dot(tk, xk, uk)
        k2 = self.__x_dot(tk + h / 2.0, xk + h * k1 / 2.0, uk)
        k3 = self.__x_dot(tk + h / 2.0, xk + h * k2 / 2.0, uk)
        k4 = self.__x_dot(tk + h, xk + h * k3, uk)

        return xk + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    def __x_dot(self, t, x, w_):
        # Estados atuais
        w = x[0:2]
        v = x[4:6]
        phi = x[6]
        ome = x[7]

        # Variáveis auxiliares
        # Forças
        f1 = self.kf * w[0] ** 2
        f2 = self.kf * w[1] ** 2
        # Torque
        Tc = self.l * (f1 - f2)
        # Força de controle
        Fc_B = np.array([[0], [(f1 + f2)]])
        # Matriz de atitude
        D_RB = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

        # Derivadas
        w_dot = (-w + w_) / self.tau
        ref_dot = v
        v_dot = (1 / self.m) * (D_RB @ Fc_B + self.Fg)
        v_dot = v_dot.reshape(
            2,
        )
        phi_dot = np.array([ome])
        ome_dot = np.array([Tc / self.Iz])

        return np.concatenate([w_dot, ref_dot, v_dot, phi_dot, ome_dot])

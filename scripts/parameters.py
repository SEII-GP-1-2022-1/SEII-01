import pygame
import numpy as np

name_bkg_img = "../sprites/background_1.jpg"
name_bkg_img_2 = "../sprites/background_2.jpg"
name_bkg_img_3 = "../sprites/background_3.jpg"
name_bkg_img_4 = "../sprites/background_4.jpg"
name_bkg_img_5 = "../sprites/background_5.jpg"
name_drone_img = "../sprites/red_drone.png"
name_drone_img_2 = "../sprites/green_drone.png"
path_drone_img = "../sprites/red_drone_transitions/"
path_drone_img_2 = "../sprites/green_drone_transitions/"

w_max = 15000.0  # velocidade máxima do motor
m = 0.25  # massa
g = 9.81  # aceleração da gravidade
l = 0.1  # tamanho
kf = 1.744e-08  # constante de força
Iz = 2e-4  # momento de inércia
tal = 0.005
Fg = np.array([[0], [-m * g]])
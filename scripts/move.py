import pygame  # Importando a pygame
from parameters import *  # Importando os parametros de variaveis definidos
from simulation import Simulation
from drone import Drone
from cmath import pi

pygame.init()  # Iniciando a pygame

bkg_img = pygame.image.load(name_bkg_img)

# Pegando o comprimento e a altura da imagem
size_width = bkg_img.get_rect().width
size_height = bkg_img.get_rect().height

# Limites da tela
size_width_m = size_width/15     
size_height_m = size_height/16

speed = 3  # [pixel/segundo]
speed_y = 0
step = 0.005    # Passo da simulação

clock = pygame.time.Clock()

def interpolate(x, x_min, x_max, y_min, y_max):
    return ((x - x_min) / (x_max - x_min) * (y_max - y_min)) + y_min

# Definindo as posições iniciais
init_pos_m = [size_width_m / 2.0, size_height_m / 2.0]
init_x = interpolate(init_pos_m[0], 0, size_width_m, 0, size_width)
init_y = interpolate(init_pos_m[1], 0, size_height_m, 0, size_height)
init_y = size_height - init_y

# Definindo os objetos da simulação e atualização do drone
sim = Simulation(step_sim=step, init_pos=init_pos_m, init_point=init_pos_m)
drone = Drone(image_path=name_drone_img, init_pos=(init_x, init_y))

# Definindo o tamanho da tela, como a largura e altura da imagem de fundo
screen = pygame.display.set_mode((size_width, size_height))

# Carregando imagem do drone
#img_drone = pygame.image.load(name_drone_img)
#img_drone_rect = img_drone.get_rect()

# Inicando a tela do jogo com o nome Drone's Move
pygame.display.set_caption("Drone's Move")

# Definindo variavel de execução
running = True

'''
def check_collision(img_drone, img_drone_rect):

    if img_drone_rect.centery <= img_drone.get_height() / 2:
        img_drone_rect.centery = int(img_drone.get_height() / 2)

    if img_drone_rect.centerx <= img_drone.get_width() / 2:
        img_drone_rect.centerx = int(img_drone.get_width() / 2)

    if img_drone_rect.centerx > size_with - img_drone.get_width() / 2:
        img_drone_rect.centerx = int(size_width - img_drone.get_width() / 2)

    if img_drone_rect.centery > size_height - img_drone.get_height() / 2:
        img_drone_rect.centery = size_height - int(img_drone.get_height() / 2)
'''

def gravity_dynamics():

    time = clock.get_time() / 1000 # pega o tempo e passa para segundos
    speed = float(Fg[1] * time)
    return speed

def speed2pixels(speed):

    pixels = speed * -5
    return pixels

# Loop de execução
while running:

    # Mostra a imagem de fundo na posicao (0 ,0)
    #screen.blit(bkg_img, (0, 0))

    # Mostra a imagem de fundo na posicao (0 ,0)
    #screen.blit(img_drone, img_drone_rect)

    # Criando evento para finalizar o pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Variavel para receber o tipo de tecla que esta sendo pressionada
    keyboard_pressed = pygame.key.get_pressed()

    # Verificando o tipo de tecla que foi pressionada
    if keyboard_pressed[pygame.K_LEFT]:
        pos_x = sim.get_pos_x() - speed
        pos_x = max(0.0, min(pos_x, size_width_m))
        sim.set_pos_x(pos_x)
          
    if keyboard_pressed[pygame.K_RIGHT]:
        pos_x = sim.get_pos_x() + speed
        pos_x = max(0.0, min(pos_x, size_width_m))
        sim.set_pos_x(pos_x)

    if keyboard_pressed[pygame.K_UP]:
        pos_y = sim.get_pos_y() + speed
        pos_y = max(0.0, min(pos_y, size_height_m))
        sim.set_pos_y(pos_y)

    if keyboard_pressed[pygame.K_DOWN]:
        pos_y = sim.get_pos_y() - speed
        pos_y = max(0.0, min(pos_y, size_height_m))
        sim.set_pos_y(pos_y)

    '''else:
        speed_y += gravity_dynamics()
        img_drone_rect.centery += speed2pixels(speed_y)
    '''

    pos_m, angle = sim.iterate()
    x_px = interpolate(pos_m[0], 0, size_width_m, 0, size_width)
    y_px = interpolate(pos_m[1], 0, size_height_m, 0, size_height)
    y_px = size_height - y_px

    drone.update(int(x_px), int(y_px), angle)
    screen.blit(bkg_img, (0, 0))
    drone.draw(screen)

    # Checando colisoes
    #check_collision(img_drone, img_drone_rect)

    #pygame.time.delay(10)
    pygame.display.update()
    clock.tick(1/step)
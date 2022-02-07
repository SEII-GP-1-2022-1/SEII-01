import pygame  # Importando a pygame
from parameters import *  # Importando os parametros de variaveis definidos

pygame.init()  # Iniciando a pygame

bkg_img = pygame.image.load(name_bkg_img)

# Pegando o compriment e a altura e o da imagem
size_with = bkg_img.get_rect().width
size_height = bkg_img.get_rect().height

speed = 10  # [pixel/segundo]
speed_y = 0
g = 9.81 # gravity acceleration [m/s²]
clock = pygame.time.Clock()

# Definindo o tamanho da tela, como a largura e altura da imagem de fundo
screen = pygame.display.set_mode((size_with, size_height))

# Carregando imagem do drone
img_drone = pygame.image.load(name_drone_img)
img_drone_rect = img_drone.get_rect()

# Inicando a tela do jogo com o nome Drone's Move
pygame.display.set_caption("Drone's Move")

# Definindo variavel de execução
running = True

def check_collision(img_drone, img_drone_rect):

    if img_drone_rect.centery <= img_drone.get_height() / 2:
        img_drone_rect.centery = int(img_drone.get_height() / 2)

    if img_drone_rect.centerx <= img_drone.get_width() / 2:
        img_drone_rect.centerx = int(img_drone.get_width() / 2)

    if img_drone_rect.centerx > size_with - img_drone.get_width() / 2:
        img_drone_rect.centerx = int(size_with - img_drone.get_width() / 2)

    if img_drone_rect.centery > size_height - img_drone.get_height() / 2:
        img_drone_rect.centery = size_height - int(img_drone.get_height() / 2)

# Loop de execução
while running:

    # Mostra a imagem de fundo na posicao (0 ,0)
    screen.blit(bkg_img, (0, 0))

    # Mostra a imagem de fundo na posicao (0 ,0)
    screen.blit(img_drone, img_drone_rect)

    # Criando evento para finalizar o pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = clock.get_time() / 1000 # pega o tempo e passa para s  
    s_y = g * time # definindo velocidade do drone por efeito da gravidade
    speed_y += s_y # velocidade do drone por efeito da gravidade mudando a cada segundo
    
    # Variavel para receber o tipo de tecla que esta sendo pressionada
    keyboard_pressed = pygame.key.get_pressed()

    # Verificando o tipo de tecla que foi pressionada
    if keyboard_pressed[pygame.K_LEFT]:
        img_drone_rect.centerx -= speed
        clock = pygame.time.Clock()
        speed_y = 0
          
    if keyboard_pressed[pygame.K_RIGHT]:
        img_drone_rect.centerx += speed
        clock = pygame.time.Clock()
        speed_y = 0

    if keyboard_pressed[pygame.K_UP]:
        img_drone_rect.centery -= speed
        clock = pygame.time.Clock()
        speed_y = 0

    if keyboard_pressed[pygame.K_DOWN]:
        img_drone_rect.centery += speed

    else:
        img_drone_rect.centery += speed_y

    # Checando colisoes
    check_collision(img_drone, img_drone_rect)

    pygame.time.delay(10)
    pygame.display.update()
    clock.tick(30)
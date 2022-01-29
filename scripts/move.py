import pygame  # Importando a pygame
from parameters import *  # Importando os parametros de variaveis definidos

pygame.init()  # Iniciando a pygame

bkg_img = pygame.image.load(name_bkg_img)

# Pegando o compriment e a altura e o da imagem
size_with = bkg_img.get_rect().width
size_height = bkg_img.get_rect().height

speed = 10  # [pixel/segundo]

# Definindo o tamanho da tela, como a largura e altura da imagem de fundo
screen = pygame.display.set_mode((size_with, size_height))

# Carregando imagem do drone
img_drone = pygame.image.load(name_drone_img)
img_drone_rect = img_drone.get_rect()

# Inicando a tela do jogo com o nome Drone's Move
pygame.display.set_caption("Drone's Move")

# Definindo variavel de execução
running = True

# Loope de execução
while running:

    # Mostra a imagem de fundo na posicao (0 ,0)
    screen.blit(bkg_img, (0, 0))

    # Mostra a imagem de fundo na posicao (0 ,0)
    screen.blit(img_drone, img_drone_rect)

    # Criando evento para finalizar o pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Variavel para receber o tipo de tecla que esta sendo pressionada
    keyboard_pressed = pygame.key.get_pressed()

    # Verificando o tipo de tecla que foi pressionada
    if keyboard_pressed[pygame.K_LEFT]:
        img_drone_rect.centerx -= speed

    if keyboard_pressed[pygame.K_RIGHT]:
        img_drone_rect.centerx += speed

    if keyboard_pressed[pygame.K_UP]:
        img_drone_rect.centery -= speed

    if keyboard_pressed[pygame.K_DOWN]:
        img_drone_rect.centery += speed

    # Checando colisoes
    if img_drone_rect.centery == 0:
        img_drone_rect.centery = size_height

    if img_drone_rect.centerx > size_with:
        img_drone_rect.centerx = size_with

    if img_drone_rect.centery > size_height:
        img_drone_rect.centery = size_height

    pygame.time.delay(10)
    pygame.display.update()

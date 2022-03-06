#!/bin/env python3
import pygame  # Importando a pygame
from parameters import *  # Importando os parametros de variaveis definidos
from simulation import Simulation
from drone import Drone
from cmath import pi
import button

pygame.init()  # Iniciando a pygame

bkg_img = pygame.image.load(name_bkg_img)

# Pegando o comprimento e a altura da imagem
size_width = bkg_img.get_rect().width
size_height = bkg_img.get_rect().height

screen = pygame.display.set_mode((size_width, size_height))

# Carregando fontes
font = pygame.font.SysFont(None, 40)
smallfont = pygame.font.SysFont(None,25)
BLACK = (0, 0, 0)

# Carregando imagens dos botões
backg_1 = pygame.image.load('../sprites_icon/background_1.jpg').convert_alpha()
backg_2 = pygame.image.load('../sprites_icon/background_2.jpg').convert_alpha()
backg_3 = pygame.image.load('../sprites_icon/background_3.jpg').convert_alpha()
backg_4 = pygame.image.load('../sprites_icon/background_4.jpg').convert_alpha()
backg_5 = pygame.image.load('../sprites_icon/background_5.jpg').convert_alpha()
drone_1 = pygame.image.load('../sprites/red_drone.png').convert_alpha()
drone_2 = pygame.image.load('../sprites/green_drone.png').convert_alpha()

#criando as instancias dos botões
backg_1_button = button.Button(120, 150, backg_1, 1)
backg_2_button = button.Button(370, 150, backg_2, 1)
backg_3_button = button.Button(620, 150, backg_3, 1)
backg_4_button = button.Button(245, 350, backg_4, 1)
backg_5_button = button.Button(495, 350, backg_5, 1)
drone_1_button = button.Button(200, 230, drone_1, 1)
drone_2_button = button.Button(550, 230, drone_2, 1)

text = font.render('Menu Principal', True, (255,255,255))
text2 = smallfont.render('Selecione um plano de fundo', True, (255,255,255))
text3 = smallfont.render('Selecione um drone', True, (255,255,255))

def bg_menu():

    screen.fill(BLACK)
 
    if backg_1_button.draw(screen):
        print('Background 1 selecionado')
        bkg_img = pygame.image.load(name_bkg_img)
    if backg_2_button.draw(screen):
        print('Background 2 selecionado')
        bkg_img = pygame.image.load(name_bkg_img_2)
    if backg_3_button.draw(screen):
        print('Background 3 selecionado')
        bkg_img = pygame.image.load(name_bkg_img_3)
    if backg_4_button.draw(screen):
        print('Background 4 selecionado')
        bkg_img = pygame.image.load(name_bkg_img_4)
    if backg_5_button.draw(screen):
        print('Background 5 selecionado')
        bkg_img = pygame.image.load(name_bkg_img_5)

    screen.blit(text, [350, 30])
    screen.blit(text2, [330, 75])
    pygame.display.flip()

def drone_menu():
    
    screen.fill(BLACK)
    screen.blit(text, [350, 30])
    screen.blit(text3, [370, 75])

    if drone_1_button.draw(screen):
        print('Drone 1 selecionado')
    if drone_2_button.draw(screen):
        print('Drone 2 selecionado')
    #pygame.draw.rect(screen, (255,255,255), [200, 230, 150, 100])
    #pygame.draw.rect(screen, (255,255,255), [550, 230, 150, 100])
    pygame.display.flip()

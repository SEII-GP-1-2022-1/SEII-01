import pygame

#Criando a classe button
class Button():
	def __init__(self, x, y, image, scale):
		#Pega o tamanho da imagem que foi carregada no menu e aplica uma escala a mesma
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		#Criando retangulos para as imagens que serão carregadas para as coordenadas especificadas no menu
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	'''Criando um "draw method" para fazer aparecer na tela as imagens
	dentro do retangulo criadas na "def __init__" das imagens que foram carregadas anteriosmente,
	e fazer com que o o usuario possa escolher com o mouse qual opção ele deseja'''
	def draw(self, surface):
		action = False
		#Pega a posição do mouse na tela
		pos = pygame.mouse.get_pos()

		'''Checa a posição em que o mouse se encontra e 
		tambem sé há colisão ou não do mesmo com as opções de imagem criadas'''
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		'''#Um teste para poder clicar varias vezes e ver se a classe esta funcionando
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False'''

		#Desenha as imagens requisitadas na tela
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
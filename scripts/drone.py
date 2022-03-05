import pygame
from cmath import pi


class Drone(pygame.sprite.Sprite):
    def __init__(self, image_path, init_pos):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.original_image = self.image
        self.rect = self.image.get_rect(center=init_pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, pos_x, pos_y, angle):
        self.rect.move_ip(pos_x - self.rect.centerx, pos_y - self.rect.centery)

        self.image = pygame.transform.rotozoom(self.original_image, angle * 180.0 / pi, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
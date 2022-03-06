import pygame
import os
from cmath import pi


class Drone(pygame.sprite.Sprite):
    def __init__(self, image_path, init_pos):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.original_image = self.image
        self.rect = self.image.get_rect(center=init_pos)

    def imgs_to_animation(self, directory):
        self.all_images = []
        for name_imgs in os.listdir(directory):
            print(name_imgs)
            img = pygame.image.load(directory + name_imgs)
            img = pygame.transform.scale(img, (64, 64))
            self.all_images.append(img)

        return self.all_images

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, pos_x, pos_y, angle, index_img):
        self.rect.move_ip(pos_x - self.rect.centerx, pos_y - self.rect.centery)

        self.image = pygame.transform.rotozoom(self.all_images[index_img], angle * 180.0 / pi, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

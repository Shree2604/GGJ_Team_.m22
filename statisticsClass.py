# Import necessary modules
import os
import pygame

# Import local modules
from abs_path import abs_path
from mainConst import screen, pixel_font

# Initialize Pygame
pygame.init()

# Global variable to track if statistics are clicked
clicked_statistics = False

class Statistics:
    def __init__(self, x, y, width, height, path, text_lg=None, text_name=None, text_days=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_lg = text_lg
        self.text_name = text_name
        self.text_days = text_days

        # Load and scale images
        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.logika_image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/logika.png')), (60, 60))

        # Set image positions
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        self.exit_rect = self.exit.get_rect(center=(96, 75))

        # Render text
        self.logiki_text = pixel_font.render(self.text_lg, True, (255, 255, 255))
        self.name_text = pixel_font.render(self.text_name, True, (255, 255, 255))
        self.days_text = pixel_font.render(self.text_days, True, (255, 255, 255))

        # Set text positions
        self.logiki_text_rect = self.logiki_text.get_rect(center=(400, 75))
        self.name_text_rect = self.name_text.get_rect(center=(400, 200))
        self.days_text_rect = self.days_text.get_rect(center=(400, 250))

    def blit_statistics(self):
        # If statistics are clicked, blit images and text to the screen
        if clicked_statistics:
            screen.blit(self.image, self.image_rect)
            screen.blit(self.logiki_text, self.logiki_text_rect)
            screen.blit(self.name_text, self.name_text_rect)
            screen.blit(self.days_text, self.days_text_rect)
            screen.blit(self.exit, self.exit_rect)
            screen.blit(self.logika_image, (430, 45))

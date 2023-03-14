
import pygame, sys, os, time, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

pygame.display.set_caption('mak gam')
screen_width=600; screen_height=400
global WINDOW_SIZE
WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) 


CHUNK_SIZE = 15 ; font = "C:/WINDOWS/FONTS/TEMPSITC.ttf"

white=(255, 255, 255); black=(0, 0, 0); gray=(50, 50, 50); red=(255, 0, 0); green=(0, 255, 0); blue=(0, 0, 255); yellow=(255, 255, 0)

#Inventory
global inventory_size
inventory_size = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

def generate_chunk(x,y):
    chunk_data = []
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos
            tile_type = 0 
            if target_y > 10:
                tile_type = 2
            elif target_y == 10:
                tile_type = 1
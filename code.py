
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
            elif target_y == 9:
                if random.randint(1,5) == 1:
                    tile_type = 3 
            if tile_type != 0:
                chunk_data.append([[target_x,target_y],tile_type])
    return chunk_data

global animation_frames
animation_frames = {}

def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame
        
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

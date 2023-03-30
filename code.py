
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



def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def mainmenu():
    
    menu=True
    selected="start"
    
    pygame.mixer.music.load('C:/Users/user/Documents/PyGameFolder/music/music.mp3')
    pygame.mixer.music.play(-1)
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        choosecharc()
                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
 

        screen.fill((52,62,67))
        title0=text_format("STUPID GAME", font, 25, (153,166,195))
        title=text_format("UP/DOWN ARROW KEY TO CHOOSE", font, 15, (153,166,195))
        title1=text_format("ENTER FOR CONFIRMATION", font, 15, (153,166,195))
        if selected=="start":
            text_start=text_format("START", font, 20, white)
        else:
            text_start = text_format("START", font, 20, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 20, white)
        else:
            text_quit = text_format("QUIT", font, 20, black)
        title0_rect=title0.get_rect()
        title_rect=title.get_rect()
        title1_rect=title1.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()



        screen.blit(title0, (screen_width/2 - (title0_rect[2]/2), 50))
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(title1, (screen_width/2 - (title1_rect[2]/2), 100))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(60)
        pygame.display.set_caption("mak gam")

def choosecharc():
    global num 
    num = 1
    pygame.mixer.music.load('C:/Users/user/Documents/PyGameFolder/music/lull.mp3')
    pygame.mixer.music.play(-1)
    menu=True
    selected="start"
    mage_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/mage.png').convert()
    mage_img.set_colorkey((255,255,255))
    gunner_img = pygame.image.load('C:/Users/user/Documents/PyGameFolder/pewpewanimation/idle/idle_0.png').convert()
    gunner_img.set_colorkey((255,255,255))
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        num = 1
                        game(num)
                    if selected=="quit":
                        num = 2
                        game(num)
                if event.key==pygame.K_ESCAPE:
                    mainmenu()


        screen.fill((52,62,67))
        title0=text_format("CHOOSE CHARACTER", font, 25, (153,166,195))
        if selected=="start":
            text_start=text_format("GUNNER", font, 20, white)
        else:
            text_start = text_format("GUNNER", font, 20, black)
        if selected=="quit":
            text_quit=text_format("MAGE", font, 20, white)
        else:
            text_quit = text_format("MAGE", font, 20, black)
        title0_rect=title0.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        screen.blit(title0, (screen_width/2 - (title0_rect[2]/2), 50))
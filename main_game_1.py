## mian game
import pygame
import keyboard
import time





running = True

pygame.init()

screen_width = 600
screen_height = 600



# Set the window size
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
falling = True



character_position = [100,500]
character_radius = 15
character_facing = "right"


class Block(pygame.sprite.Sprite):
    def __init__(self,character_position, character_radius):

        x = character_position[0]
        y = character_position[1]
        z = character_radius

        pygame.draw.circle(screen, (0, 0, 0),(x, y),z)
        pygame.display.update()

class boundary:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, width, height))
        pygame.display.update()

def background():
    screen.fill((255, 255, 255))
    draw_level(levels, current_level)
    

def draw_level(levels, current_level):
    for boundary in levels[current_level]:
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(boundary.x, boundary.y, boundary.width, boundary.height))
           
def side_walls(character_position, character_radius):
    if character_position[0] + 50 + character_radius >= screen_width:
        character_position[0] = screen_width - character_radius



        
def accelleration(character_facing, character, character_position, character_radius, falling):
    jump = True
    accelleration = 20
    side = 50
    while accelleration > 0 :
            

            time.sleep(0.05)
            background()
            character = Block(character_position, character_radius)

def touching_vertically(character_position, character_radius, boundary, falling):
    for boundary in levels[current_level]:
        if character_position[1] + character_radius*2 >= boundary.y and character_position[1] <= boundary.y + boundary.height \
            and character_position[0] >= boundary.x and character_position[0] <= boundary.x + boundary.width \
            and falling:
            character_position[1] = boundary.y - character_radius*2 + 1
            falling = False
            print(character_position[1],falling)
            return falling
            


level1 = [
boundary(0,580,600,20),

]


current_level = 0
levels = [level1]



while running:
    print(falling)
    # Fill the background with white
    character = Block(character_position, character_radius)
    background()
    character = Block(character_position, character_radius)

    fps = pygame.time.Clock()
    
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keyboard.is_pressed('left'):
        falling = True
        accelleration("left",character, character_position, character_radius, falling)
    if keyboard.is_pressed('right'):
        falling = True
        accelleration("right",character, character_position, character_radius, falling)

    print(falling)
    touching_vertically(character_position, character_radius, level1, falling)
    print(falling)
    if falling == True and character_position[1] < screen_height - character_radius:
        character_position[1] += 10

    pygame.display.update() 
#создай игру "Лабиринт"!
from pygame import *
windows = display.set_mode((700,500))
background = transform.scale(image.load("303030.jpg"),(700,500))
display.set_caption('Лабиринт')
class gamesprite(sprite.Sprite):
    def __init__(self,image1,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(image1),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        windows.blit(self.image,(self.rect.x,self.rect.y))


class Player (gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
class Player2 (gamesprite):
    derektion = "left"
    def update(self):
        if self.rect.x <= 500:
            self.derektion = "left"
            
        if self.rect.x >= 680:
            self.derektion = "right"
            
        if self.derektion == "left":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

            
class wlan(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill(color_1,color_2,color_3)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        windows.blit(self.image,(self.rect.x,self.rect.y))

        



hero1 =Player2('cyborg.png',3,600,250)
hero = Player('hero.png',5,100,150)
hero2 =gamesprite('treasure.png',5,600,400)
game = True
mixer.init()
mixer.music.load('33.mp3')
mixer.music.play()
while game:

    windows.blit(background,(0,0))
    hero.update()
    hero1.update()
    hero.reset()
    hero1.reset()
    hero2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if e != True:
        windows.blit(background,(0,0))
        hero.update()
        hero1.update()
        hero.reset()
        hero1.reset()
    
    display.update()
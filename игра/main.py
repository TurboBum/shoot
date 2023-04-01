from pygame import *
from random import randint



background = transform.scale(image.load("002.jpg"),(1000,1000))

windows = display.set_mode((1000, 1000))


class gamesprite(sprite.Sprite):

    def __init__(self,image1,speed,x,y,proverka):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.proverka = proverka

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))




class prepatstvie(gamesprite):
    def update(self):
        hits = sprite.groupcollide(bullets,bads, True, True) 
        for hit in hits:
            bullets.remove(Bullet)



class player(gamesprite):
    def update(self):
        
        keys = key.get_pressed()
        
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.q = "bullet.png"
            self.proverka = 1
        if keys[K_s] and  self.rect.y < 950:
            self.rect.y += self.speed
            self.q = "bullet2.png"
            self.proverka = 2
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.q = "bullet3.png"
            self.proverka = 3
        if keys[K_d] and self.rect.x < 950:
            self.rect.x += self.speed
            self.proverka = 4
            self.q = "bullet1.png"


            

    def shoot(self):
        bullet = Bullet(self.q, 3, self.rect.x, self.rect.y, self.proverka)
        bullets.add(bullet)

        

class Bullet (gamesprite):
    def update(self):
        #print(self.proverka)
        if self.proverka == 1 :
            self.rect.y -= self.speed
        elif self.proverka == 2 :
            self.rect.y += self.speed
        elif self.proverka == 3 :
            self.rect.x -= self.speed
        elif self.proverka == 4 :
            self.rect.x += self.speed
        if self.rect.y < 0:
            self.kill()
         


bullets = sprite.Group()
all_sprites = sprite.Group()
bads = sprite.Group()

hero = player('1.jpg', 1, 275, 250,0)
kamen = prepatstvie('asteroid.png', 1, 300, 400,0)
bads.add(kamen)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.shoot()
    
    windows.blit(background, (0, 0))
    hero.update()
    hero.reset()
    kamen.update()
    kamen.reset()
    bullets.draw(windows)
    bullets.update()
    display.update()












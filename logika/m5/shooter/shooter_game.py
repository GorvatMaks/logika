#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


mixer.init()

mixer.music.load("space.ogg")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)



wind_wid = 700
wind_hei = 500
window = display.set_mode((wind_wid, wind_hei))

lost = 0 
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_width, player_haight, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_haight))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < wind_wid - 89:
            self.rect.x += self.speed       

    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
        global lost
        
        if self.rect.y > wind_hei:
            self.rect.y = 0
            self.rect.x = randint(0, wind_wid-80)
            lost = lost + 1

backgroun = scale(load("galaxy.jpg"), (wind_wid, wind_hei))

rocket = Player("rocket.png", 350, wind_hei - 100, 85, 100, 6)

ens = sprite.Group()
for i in range(5):
    x = randint(0, wind_wid - 80)
    y = 0
    speed = randint(1,3)

    mon = Enemy("ufo.png",x, y , 80, 50, speed)

    ens.add(mon)



FPS = 60
clock = time.Clock()
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.blit(backgroun, (0, 0))
        txt_lose = font1.render(f'Пропущен: {lost}', True, (255,53,43))
        window.blit(txt_lose, (10, 50))
        txt_win = font2.render(f'Рахунок: {score}', True, (53,255,43))
        window.blit(txt_win, (10, 20))


        ens.draw(window)
        ens.update()

        rocket.reset()
        rocket.update()
    
    display.update()
    clock.tick(FPS)
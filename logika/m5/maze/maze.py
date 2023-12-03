#створи гру "Лабіринт"!
from typing import Any
from pygame import *

from pygame.transform import scale, flip
from pygame.image import load
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed


class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
        if self.rect.x <= 350:
            self.direction = "right"

        if self.rect.x >= win_width - 180:
            self.direction = "left"

class Wall(sprite.Sprite):
    def __init__(self, wall_x , wall_y, wall_width, wall_haight):
        super().__init__()
        self.width = wall_width
        self.haight = wall_haight
        
        self.image = Surface((self.width, self.haight))
        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

        self.image.fill((128, 0, 128))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
background = scale(load('background.jpg'), (win_width, win_height))

wall_1 = Wall(90, 15 , 15 , 320 )
wall_2 = Wall(90, 15 , 610 , 15 )
wall_3 = Wall(205, 315 , 15 , 198 )
wall_4 = Wall(90, 220 , 132 , 10 )
wall_5 = Wall(215, 120 , 382 , 10 )
wall_6 = Wall(0, 325 , 100 , 10 )
wall_7 = Wall(587, 130 , 10 , 298 )
wall_8 = Wall(587, 130 , 10 , 298 )
wall_9 = Wall(307, 130 , 10 , 195 )
wall_10 = Wall(207, 315 , 300 , 10)
wall_11 = Wall(305, 420 , 288 , 10 )


player = Player("hero.png", 5, win_height - 83, 5 )
monster = Enemy("cyborg.png",win_width - 320,win_height - 250, 3)
treasure = GameSprite("treasure.png", win_width - 250, win_height - 350, 0 )

walls = [wall_1,wall_2,wall_3,wall_4,wall_5,wall_6,wall_7,wall_8,wall_9,wall_10,wall_11]


clock =time.Clock()
FPS = 60 

game = True
finish = False

font.init()
f = font.Font(None, 70)

win = f.render('YOU WIN!', False, (255, 215, 0 ))
lose = f.render('YOU LOSE!', False, (255, 1 , 15))


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    for wall in walls:
        wall.reset()

    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        treasure.reset()
        player.update()
        wall_1.reset()
        wall_2.reset()
        wall_3.reset()
        wall_4.reset()
        wall_5.reset()
        wall_6.reset()
        wall_7.reset()
        wall_8.reset()
        wall_9.reset()
        wall_10.reset()
        wall_11.reset()

        monster.update()

        treasure.update()


        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            money_sound.play()



        for wall in walls:
            if sprite.collide_rect(player, wall) or sprite.collide_rect(player, monster):
                finish = True
                window.blit(lose, (200, 200))
                kick_sound.play()

        display.update()
        clock.tick(FPS)
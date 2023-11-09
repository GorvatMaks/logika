from pygame import*
#Вікно
window = display.set_mode((700,500))
backgound = transform.scale(image.load("background.png"),(700, 500))
#Вікно завершене

clock = time.Clock()
Fps = 60

speed = 10

#Створення спрайтів)
sprite1 = transform.scale(image.load("sprite1.png"),(100, 100))
x1 = 100
y1 = 400

sprite2 = transform.scale(image.load("sprite2.png"),(100, 100))
x2 = 300 
y2 = 299



#Цикил
game = True

while game:
    window.blit(backgound, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    #Обробка Подій
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_LEFT]and x1 > 5:
        x1 -= speed

    if keys_pressed[K_RIGHT]and x1 < 600:
        x1 += speed

    if keys_pressed[K_UP]and y1 > 5:
        y1 -= speed

    if keys_pressed[K_DOWN]and y1 < 400:
        y1 += speed



    if keys_pressed[K_a]and x2 > 5:
        x2 -= speed

    if keys_pressed[K_d]and x2 < 600:
        x2 += speed

    if keys_pressed[K_w]and y2 > 5:
        y2 -= speed

    if keys_pressed[K_s]and y2 < 400:
        y2 += speed

    display.update()
    clock.tick(Fps)
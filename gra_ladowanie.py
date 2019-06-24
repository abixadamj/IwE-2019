# Tutaj pisz swój kod, młody padawanie ;-)
from random import randint
from time import sleep
from sys import exit

WIDTH = 1000
HEIGHT = 667

LANDING_ZONE = randint(700,900)
RED = 200, 0, 0
BOX = Rect((LANDING_ZONE, 660), (50, 10))

MAX_X = 5 # maksymalne przemieszczenie się obiektu - im większe, tym trudniejsza gra

background_active = 'beach-tlo.jpg'
background_position = (0,0)

win = Actor('fireworks.jpg')
win.x = 450
win.y = 300

hero = Actor('drone-png-small.png')
hero.x = randint(0,20)
hero.y = randint(0,20)    # ustalamy początkową pozycję naszego bohatera x,y

# global ;-)
gra_trwa = True
gra_wygrana = False
dron_x = randint(1, MAX_X)

def update():
    global gra_trwa, dron_x, gra_wygrana
    screen.blit( background_active, background_position ) #rysowanie tła
    screen.draw.filled_rect(BOX, RED) # rysowanie lądowiska
    odleglosc = hero.distance_to((LANDING_ZONE, 660))
    screen.draw.text('Do obiektu: '+str(odleglosc), (20, 650), fontsize=20)
    if gra_trwa:
        hero.x += dron_x # za każdym razem przesuwamy naszego drona
    # teraz sprawdzamy klawiaturę
    if keyboard.r == 1:
        hero.x = randint(0,20)
        hero.y = randint(0,20)    # ustalamy początkową pozycję naszego bohatera x,y
        gra_trwa = True
        gra_wygrana = False
    if keyboard.q == 1:
        exit()
    if keyboard.up == 1:
        hero.y -= 3
    if keyboard.down == 1:
        hero.y += 3
    if hero.x > LANDING_ZONE+120:
        screen.draw.text('GAME OVER ;-)', (20, 100), fontsize=60)
        screen.draw.text('R to restart', (20, 150), fontsize=60)
        screen.draw.text('Q to quit', (20, 200), fontsize=60)
        gra_trwa = False
    if hero.colliderect(BOX):
        # sleep(2)
        gra_trwa = False
        gra_wygrana = True

def draw():
    global gra_wygrana
    hero.draw()
    if gra_wygrana:
        win.draw()
        screen.draw.text('YOU WIN ;-)', (20, 100), color=(200, 200, 200), fontsize=60)
import math
import random
import pygame
screen_width=800
screen_height=500
playerstartx=370
playerstarty=380
enemystartymininmum=50
enemystartymaximum=150
enemyspeedx=4
enemyspeedy=40
bulletspeedy=10
collisiondistance=27
pygame.init()
screen=pygame.display.set_mode(screen_width,screen_height)
background=pygame.image.load("gamebackground.JPG")
pygame.display.set_caption("Space Invertor")
icon=pygame.image.load("Rocket.JPEG")
pygame.display.set_icon(icon)
playerimg=pygame.image.load("Rocket.JPEG")
playerx=playerstartx
playery=playerstarty
playerexchange=0
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numberofenemies=6
for _i in range(numberofenemies):
    enemyimg.append(pygame.image.load("target.jpeg"))
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemystartymininmum,enemystartymaximum))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)
bulletimg=pygame.immage.load("bullet.jpg")
bulletx=0
bullety=playerstarty
bulletxchange=0
bulletychange=bulletspeedy
bulletspeed=("ready")
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
def showscore(x,y):
    score=font.render("score: "+str(score_value),True,(255,255,255))
    screen.blint(score,(x,y))
def gameovertext():
    overtext=over_font.render("Game Over!!",True,(255,255,255))
    screen.blint(overtext,(200,250))
def player(x,y):
    screen.blint(playerimg,(x,y))
def enemy(x,y,i):
    screen.blint(enemyimg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blint(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
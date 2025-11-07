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
playerimg=pygame.image.load(icon)

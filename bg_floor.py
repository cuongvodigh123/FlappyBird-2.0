# mặt đất

import pygame, sys, random, time,threading  
class BG_FL:
    def __init__(self,screen):
        self.screen = screen
        
        self.a=1
        self.ok=True
        
        self.bg= pygame.image.load('assets/background-night.png').convert()
        self.bg = pygame.transform.scale2x(self.bg)
        
        self.bg1= pygame.image.load('assets/background-dark.png').convert()
        self.bg1 = pygame.transform.scale2x(self.bg1)
        
        self.floor= pygame.image.load('assets/floor.png').convert()
        self.floor= pygame.transform.scale2x(self.floor)
        self.floor_x=0
        self.floor_top=pygame.image.load('assets/floor-top.png')
        self.floor_top_sunface=self.floor_top.get_rect(midleft=(0,-7))

        self.floor_bot=pygame.image.load('assets/floor-bot.png')
        self.floor_bot_sunface=self.floor_bot.get_rect(midleft=(0,660))
    def update_bg(self):
        if self.a %2==0:
            self.screen.blit(self.bg1,(0,0))
        elif self.a %2==1:
            self.screen.blit(self.bg,(0,0))
    def ve_san(self):
        self.screen.blit(self.floor,(self.floor_x,650))
        self.screen.blit(self.floor,(self.floor_x+672,650))  
    def move_san(self):
        self.floor_x -=2
        self.ve_san()
        if self.floor_x <=-432:
            self.floor_x=0
    
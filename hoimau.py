# cơ chế tương tụ bom
import pygame, sys, random, time,threading  
class HoiMau:
    def __init__(self,screen):
        self.pause = True
        self.screen = screen
        self.b=0
        self.mau_sunface = pygame.image.load('assets/hoimau.png').convert_alpha()
        self.mau_list= []
        self.mau_height=[50,100,150,200]
    def add_mau(self):
        if self.pause == True:
            if self.b==300:
                self.create_mau()
                self.b=0
            self.b+=1
    def create_mau(self):
        random_mau_pos = random.choice(self.mau_height)
        bottom_mau = self.mau_sunface.get_rect(center= (900,random_mau_pos*2))
        self.mau_list.append(bottom_mau)
    def move_mau(self):
        if self.pause == True:
            for mau in self.mau_list :
                mau.centerx -= 2
                
    def draw_mau(self):
        for mau in self.mau_list:
            self.screen.blit(self.mau_sunface,mau)
        
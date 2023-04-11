# bom
import pygame, sys, random, time,threading  
class Bom:
    def __init__(self,screen):
        self.pause = True
        self.screen = screen
        self.b=-10
        self.bom_sunface = pygame.image.load('assets/boom.png').convert_alpha()
        self.bom_list= []
        self.bom_height=[0,50,100,150,200,250]
    # thêm bom vào hàng chờ
    def add_bom(self):
        if self.pause == True:
            if self.b==145:
                self.create_bom()
                self.b=-10
            self.b+=1
    # tạo bom mỗi thời gian 
    def create_bom(self):
        random_bom_pos = random.choice(self.bom_height)
        bottom_bom = self.bom_sunface.get_rect(center= (random_bom_pos*2,10))
        self.bom_list.append(bottom_bom)
    #  di chuyển
    def move_bom(self):
        if self.pause == True:
            for bom in self.bom_list :
                bom.centery += 1.4
    def draw_bom(self):
        for bom in self.bom_list:
            self.screen.blit(self.bom_sunface,bom)
        
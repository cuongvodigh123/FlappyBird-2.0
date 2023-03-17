import pygame, sys, random, time,threading  
class Bom:
    def __init__(self,screen):
        self.screen = screen
        self.b=-10
        self.bom_sunface = pygame.image.load('assets/boom.png').convert_alpha()
        self.bom_list= []
        self.spawnbom = pygame.USEREVENT+2
        self.delay_bom=1000
        pygame.time.set_timer(self.spawnbom, self.delay_bom)
        self.bom_height=[50,100,150,200,250]
    def add_bom(self):
        if self.b>150:
            self.create_bom()
        self.b=-10 
    def create_bom(self):
        random_bom_pos = random.choice(self.bom_height)
        bottom_bom = self.bom_sunface.get_rect(center= (random_bom_pos*2,10))
        self.bom_list.append(bottom_bom)
    def move_bom(self):
        for bom in self.bom_list :
            bom.centery += 1.4 
        self.b+=2.3
    def draw_bom(self):
        for bom in self.bom_list:
            self.screen.blit(self.bom_sunface,bom)
        
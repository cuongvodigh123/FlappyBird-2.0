import pygame, sys, random, time,threading  
from sound import *
from heal import Heal
class Bird:
    def __init__(self,screen,bird_movement,a,b,c,d):
        self.screen=screen
        self.bird_movement=bird_movement
        self.birdflap=pygame.USEREVENT +1
        pygame.time.set_timer(self.birdflap, 300)
        self.bird_index = 0    
        self.bird_down= pygame.image.load(a).convert_alpha()
        self.bird_mid= pygame.image.load(b).convert_alpha()
        self.bird_up= pygame.image.load(c).convert_alpha()
        self.bird_list=[self.bird_down,self.bird_mid,self.bird_up]
        self.bird=self.bird_list[self.bird_index]
        self.bird_rect=self.bird.get_rect(center=(100,384))
        self.mau=3
        if d=="yellow":
            self.heal = Heal(100,20)
        else:
            self.heal = Heal(620,20)
    def start(self):
        self.bird_movement=0
        self.bird_rect.center=(100,324)
        self.heal.heal_index = 3
        self.mau=3
    def fall(self,gravity):
        self.bird_movement += gravity
        self.bird_rect.centery += self.bird_movement
        self.rotate_bird()
    def bird_animation(self):
        # chim 1
        if self.bird_index < 2:
            self.bird_index +=1
        else:  
            self.bird_index = 0  
        new_bird = self.bird_list[self.bird_index]
        new_bird_rect = new_bird.get_rect(center= (self.bird_rect.centerx,self.bird_rect.centery))
        
        self.bird, self.bird_rect =new_bird, new_bird_rect
    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(self.bird,-self.bird_movement*4,1)
        self.heal.heal_index = self.mau 
        self.heal.heal = self.heal.heal_list[self.heal.heal_index]
        self.screen.blit(self.heal.heal,self.heal.heal_rect)
        self.screen.blit(new_bird,self.bird_rect)
    def check_collision(self,pipes,boms,floor_top_sunface,floor_bot_sunface):
        for bom in boms:
            if self.bird_rect.colliderect(bom):
                self.bird_movement=1
                hit()
                return False
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                self.bird_movement=1
                hit()
                return False
        if self.bird_rect.centery <=0 or self.bird_rect.centery >=650:
                return False
        if self.bird_rect.colliderect(floor_top_sunface) or self.bird_rect.colliderect(floor_bot_sunface):
                self.bird_movement=1
                hit()
                return False
        return True
    
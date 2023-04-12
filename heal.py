import pygame, sys, random, time,threading
class Heal:
    def __init__(self,x,y):
        self.heal0 = pygame.image.load("assets/nothing.png").convert_alpha()
        self.heal1 = pygame.image.load("assets/heal1.png").convert_alpha()
        self.heal2 = pygame.image.load("assets/heal2.png").convert_alpha()
        self.heal3 = pygame.image.load("assets/heal3.png").convert_alpha()
        self.heal_index = 3
        self.heal_list = [self.heal0,self.heal1,self.heal2,self.heal3]
        self.heal = self.heal_list[self.heal_index]
        self.heal_rect = self.heal.get_rect(midleft=(x,y))
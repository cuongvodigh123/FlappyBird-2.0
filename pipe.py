import pygame, sys, random, time,threading  
class Pipe:
    def __init__(self,screen):
        self.a=850
        self.screen=screen
        self.pipe_sunface = pygame.image.load('assets/pipe-green.png').convert()
        self.pipe_sunface= pygame.transform.scale2x(self.pipe_sunface)
        self.pipe_list= []
        self.spawnpipe = pygame.USEREVENT
        self.speed=1500
        pygame.time.set_timer(self.spawnpipe, self.speed)
        self.pipe_height=[250,300,350,400,450,500,535]
    def add_pipe(self):
        if self.a<700:
            self.create_pipe()
        self.a=900
    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_sunface.get_rect(midtop= (900,random_pipe_pos))
        top_pipe = self.pipe_sunface.get_rect(midtop= (900,random_pipe_pos-650))
        self.pipe_list.extend((bottom_pipe, top_pipe))
    def move_pipe(self):
        for pipe in self.pipe_list :
            pipe.centerx -= 1.2
        self.a-=5
    def draw_pipe(self):
        for pipe in self.pipe_list:
            if pipe.bottom >= 600:
                self.screen.blit(self.pipe_sunface,pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_sunface,False,True)
                self.screen.blit(flip_pipe,pipe)
    
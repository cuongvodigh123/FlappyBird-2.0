import pygame, sys, random, time,threading
game_font = pygame.font.Font('04B_19.ttf',40)
class TT:
    def __init__(self,screen):
        self.screen = screen
        self.message_sunface = pygame.image.load('assets/message.png').convert_alpha()
        self.message_sunface = pygame.transform.scale2x(self.message_sunface)
        self.message=self.message_sunface.get_rect(center=(432,374))
        
        self.message_sunface1 = pygame.image.load('assets/message1chim.png').convert_alpha()
        self.message_sunface1 = pygame.transform.scale2x(self.message_sunface1)
        self.message1=self.message_sunface1.get_rect(center=(432,374))
        
        self.gameover=pygame.image.load('assets/gameover.png').convert_alpha()
        self.gameover=pygame.transform.scale2x(self.gameover)
        self.gameover_sunface=self.gameover.get_rect(center=(400,400))

        self.tamdung=pygame.image.load('assets/pause.png').convert_alpha()
        self.tamdung_sunface=self.tamdung.get_rect(center=(400,400))
    def delay_dead(self,bg_fl):
        self.screen.blit(self.gameover,self.gameover_sunface)
        self.screen.blit(bg_fl.floor,(bg_fl.floor_x,650))
        self.screen.blit(bg_fl.floor,(bg_fl.floor_x+672,650)) 
        pygame.event.pump()
        pygame.display.flip()
        pygame.time.delay(1000)
    def number_player(self,quantity_player):
        number_sunface = game_font.render(f'{quantity_player} player',True,(223, 20, 87))
        number_rect = number_sunface.get_rect(center=(430,580))
        self.screen.blit(number_sunface,number_rect)
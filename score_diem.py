import pygame, sys, random, time,threading
game_font = pygame.font.Font('04B_19.ttf',40)
class Score:
    def __init__(self):
        self.score = 0
        self.score1 = 0
        self.hight_score=0
        self.number_score=10
    def score_display(self,screen,state,quantity_player):
        if state== 'game alive':
            score_sunface = game_font.render(str(int(self.score)),True,(255,255,0))
            score_rect = score_sunface.get_rect(center=(200,100))
            screen.blit(score_sunface,score_rect)
            if quantity_player==2:
                score_sunface1 = game_font.render(str(int(self.score1)),True,(255,0,0))
                score_rect1 = score_sunface1.get_rect(center=(650,100))
                screen.blit(score_sunface1,score_rect1)
            
        if state== 'game over':
            score_sunface = game_font.render(f'Score: {int(self.score)}',True,(255,255,0))
            score_rect = score_sunface.get_rect(center=(200,100))
            screen.blit(score_sunface,score_rect)
            if quantity_player==2:
                score_sunface1 = game_font.render(f'Score: {int(self.score1)}',True,(255,0,0))
                score_rect1 = score_sunface1.get_rect(center=(650,100))
                screen.blit(score_sunface1,score_rect1)

            hight_score_sunface = game_font.render(f'Hight Score: {int(self.hight_score)}',True,(255,255,255))
            hight_score_rect = hight_score_sunface.get_rect(center=(430,620))
            screen.blit(hight_score_sunface,hight_score_rect)
    def update_score(self,quantity_player):
        if self.score > self.hight_score:
            self.hight_score=self.score
        if quantity_player==2:
            if self.score1 > self.hight_score:
                self.hight_score=self.score1
        self.score=0
        self.score1=0
        self.number_score=10
        return self.hight_score
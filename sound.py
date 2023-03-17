import pygame, sys, random, time,threading  
pygame.mixer.pre_init(frequency=44100,size=-16, channels=2, buffer=512)
pygame.init()
def nhacnen(x):
    pygame.mixer.music.load('sound/nhac.wav')
    pygame.mixer.music.play(-1)
    if x == 0:
        pygame.mixer.music.unpause()
    if x == 1:
        pygame.mixer.music.pause()

def swooshing():
    sfx_swooshing_sound = pygame.mixer.Sound('sound/sfx_swooshing.wav')
    sfx_swooshing_sound.play()
def flap():
    flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
    flap_sound.play()
def score_sound():
    score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
    score_sound.play()
def hit():
    hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
    hit_sound.play()

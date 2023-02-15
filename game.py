import pygame, sys, random

def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_sunface.get_rect(midtop= (450,random_pipe_pos))
    top_pipe = pipe_sunface.get_rect(midtop= (450,random_pipe_pos-740))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 3
        if pipe.centerx <=100 and pipe.centerx >=98:
            score_sound.play()

    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_sunface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_sunface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >=650:
            hit_sound.play()
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*4,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center= (100,bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'main game':
        score_sunface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_sunface.get_rect(center = (216,100))
        screen.blit(score_sunface,score_rect)
    if game_state == 'game over':
        score_sunface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_sunface.get_rect(center = (216,100))
        screen.blit(score_sunface,score_rect)

        hight_score_sunface = game_font.render(f'Hight Score: {int(hight_score)}',True,(255,255,255))
        hight_score_rect = hight_score_sunface.get_rect(center = (216,600))
        screen.blit(hight_score_sunface,hight_score_rect)
def update_score(score,hight_score):
    if score > hight_score:
        hight_score=score
    return hight_score


pygame.mixer.pre_init(frequency=44100,size=-16, channels=2, buffer=512)
pygame.init()
screen= pygame.display.set_mode((432,768))
clock= pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF',40)
# biến
score = 0
hight_score=0
gravity = 0.15
bird_movement = 0
game_active = False
# background
bg= pygame.image.load('assets/background-night.png').convert()
bg= pygame.transform.scale2x(bg)

# sàn
floor= pygame.image.load('assets/floor.png').convert()
floor= pygame.transform.scale2x(floor)
floor_x_pos = 0
# chim
bird_down= pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
bird_mid= pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird_up= pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
bird_list=[bird_down,bird_mid,bird_up]
bird_index = 0
bird=bird_list[bird_index]
#bird= pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
#bird= pygame.transform.scale2x(bird)
bird_rect=bird.get_rect(center = (100,384))
# timer cho bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 300)
# ống
pipe_sunface = pygame.image.load('assets/pipe-green.png').convert()
pipe_sunface= pygame.transform.scale2x(pipe_sunface)
pipe_list= []
# tạo timer cho ong
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1500)
pipe_height = [150,200,300,400,250,350,450,500,530]
#end game
game_over_sunface= pygame.image.load('assets/message.png').convert_alpha()
game_over_rect = game_over_sunface.get_rect(center = (216,384))
# sound
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
sfx_swooshing_sound = pygame.mixer.Sound('sound/sfx_swooshing.wav')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0 
                bird_movement = -5
                flap_sound.play()
                sfx_swooshing_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_rect.center=(100,384)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index +=1
            else:
                bird_index = 0    
            bird, bird_rect = bird_animation()

    screen.blit(bg,(0,0))
    if game_active:
        #chim
        bird_movement+=gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement 
        screen.blit(rotated_bird,bird_rect)
        game_active=check_collision(pipe_list)
        #ong
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        #score
        for pipe in pipe_list:
            if pipe.centerx <=100 and pipe.centerx >=98:
                score += 0.5

        score_display('main game')
    else:
        screen.blit(game_over_sunface,game_over_rect)
        hight_score=update_score(score,hight_score)
        score_display('game over')  
    #floor
    floor_x_pos -=2
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
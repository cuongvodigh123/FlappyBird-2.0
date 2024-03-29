from asyncio.windows_events import NULL

try:
    
    import pygame, sys, random, time,threading   
    def delay_dead():
        hit_sound.play()
        screen.blit(gameover,gameover_sunface)
        screen.blit(floor,(floor_x,650))
        screen.blit(floor,(floor_x+672,650)) 
        pygame.event.pump()
        pygame.display.flip()
        pygame.time.delay(1000)
    def create_bom():
        random_bom_pos = random.choice(bom_height)
        bottom_bom = bom_sunface.get_rect(center= (random_bom_pos*2,10))
        return bottom_bom
    b=-10
    def move_bom(boms):
        global b
        for bom in boms :
            bom.centery += 1.4 
            
        b+=2.3
        return boms

    def draw_bom(boms):
        for bom in boms:
            screen.blit(bom_sunface,bom)
    def ve_san():
        screen.blit(floor,(floor_x,650))
        screen.blit(floor,(floor_x+672,650))  
    def create_pipe():
        random_pipe_pos = random.choice(pipe_height)
        bottom_pipe = pipe_sunface.get_rect(midtop= (900,random_pipe_pos))
        top_pipe = pipe_sunface.get_rect(midtop= (900,random_pipe_pos-650))
        return bottom_pipe, top_pipe
    a=850
    def move_pipe(pipes):
        global a
        for pipe in pipes :
            pipe.centerx -= 1.2
        a-=5
        return pipes
    def draw_pipe(pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:
                screen.blit(pipe_sunface,pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_sunface,False,True)
                screen.blit(flip_pipe,pipe)
    def rotate_bird(bird):
        new_bird = pygame.transform.rotozoom(bird,-bird_movement*4,1)
        return new_bird          
    def rotate_bird1(bird1):
        new_bird = pygame.transform.rotozoom(bird1,-bird_movement*4,1)
        return new_bird
    def bird_animation():
        # chim 1
        new_bird = bird_list[bird_index]
        new_bird_rect = new_bird.get_rect(center= (bird_rect.centerx,bird_rect.centery))
        #chim 2
        new_bird1 = bird_list1[bird_index]
        new_bird_rect1 = new_bird1.get_rect(center= (bird_rect1.centerx,bird_rect1.centery))
        
        return new_bird, new_bird_rect, new_bird1, new_bird_rect1
    def check_collision(pipes,boms):
        global bird_movement
        for bom in boms:
            if bird_rect.colliderect(bom):
                # pass
                hit_sound.play()
                bird_movement=1
                return False
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                # pass
                hit_sound.play()
                bird_movement=1
                return False
        if bird_rect.colliderect(floor_top_sunface) or bird_rect.colliderect(floor_bot_sunface):
                hit_sound.play()
                bird_movement=1
                return False
        return True
    def check_collision1(pipes,boms):
        global bird_movement1
        for bom in boms:
            if bird_rect1.colliderect(bom):
                # pass
                hit_sound.play()
                bird_movement1=1
                return False
        for pipe in pipes:
            if bird_rect1.colliderect(pipe):
                # pass
                hit_sound.play()
                bird_movement1=1
                return False
        if bird_rect1.colliderect(floor_top_sunface) or bird_rect1.colliderect(floor_bot_sunface):
                hit_sound.play()
                bird_movement1=1
                return False
        return True
    def score_display(state):
        if state== 'game alive':
            score_sunface = game_font.render(str(int(score)),True,(255,255,0))
            score_rect = score_sunface.get_rect(center=(200,100))
            screen.blit(score_sunface,score_rect)
            
            score_sunface1 = game_font.render(str(int(score1)),True,(255,0,0))
            score_rect1 = score_sunface1.get_rect(center=(650,100))
            screen.blit(score_sunface1,score_rect1)
            
        if state== 'game over':
            score_sunface = game_font.render(f'Score: {int(score)}',True,(255,255,0))
            score_rect = score_sunface.get_rect(center=(200,100))
            screen.blit(score_sunface,score_rect)
            
            score_sunface1 = game_font.render(f'Score: {int(score1)}',True,(255,0,0))
            score_rect1 = score_sunface1.get_rect(center=(650,100))
            screen.blit(score_sunface1,score_rect1)

            hight_score_sunface = game_font.render(f'Hight Score: {int(hight_score)}',True,(255,255,255))
            hight_score_rect = hight_score_sunface.get_rect(center=(430,620))
            screen.blit(hight_score_sunface,hight_score_rect)
    def update_score(score,hight_score):
        if score > hight_score:
            hight_score=score
        if score1 > hight_score:
            hight_score=score1
        return hight_score
    def unpause():
        global pause
        pygame.mixer.music.unpause()
    def paused():
        pygame.mixer.music.pause()


    pygame.mixer.pre_init(frequency=44100,size=-16, channels=2, buffer=512)
    pygame.init()
    screen = pygame.display.set_mode((864,768))
    pygame.display.set_caption("Flappy Bird 2.0")
    clock=pygame.time.Clock()
    game_font = pygame.font.Font('04B_19.ttf',40)

    score = 0
    score1 = 0
    
    hight_score=0
    gravity = 0.09
    bird_movement = 0
    bird_movement1 = 0

    message_sunface = pygame.image.load('assets/message.png').convert_alpha()
    message_sunface = pygame.transform.scale2x(message_sunface)
    message=message_sunface.get_rect(center=(432,374))

    bg= pygame.image.load('assets/background-night.png').convert()
    bg = pygame.transform.scale2x(bg)
    floor= pygame.image.load('assets/floor.png').convert()
    floor= pygame.transform.scale2x(floor)
    floor_x=0

    pipe_sunface = pygame.image.load('assets/pipe-green.png').convert()
    pipe_sunface= pygame.transform.scale2x(pipe_sunface)
    pipe_list= []
    spawnpipe = pygame.USEREVENT
    speed=1500
    pygame.time.set_timer(spawnpipe, speed)
    pipe_height=[250,300,350,400,450,500,535]
    # both
    bird_index = 0    
    # bird 0
    bird_down= pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
    bird_mid= pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
    bird_up= pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
    bird_list=[bird_down,bird_mid,bird_up]
    bird=bird_list[bird_index]
    bird_rect=bird.get_rect(center=(100,384))

    # bird 1
    bird_down1= pygame.image.load('assets/redbird-downflap.png').convert_alpha()
    bird_mid1= pygame.image.load('assets/redbird-midflap.png').convert_alpha()
    bird_up1= pygame.image.load('assets/redbird-upflap.png').convert_alpha()
    bird_list1=[bird_down1,bird_mid1,bird_up1]
    bird1=bird_list1[bird_index]
    bird_rect1=bird.get_rect(center=(100,400))   
    
    birdflap=pygame.USEREVENT +1
    pygame.time.set_timer(birdflap, 300)
    
     # boom
    bom_sunface = pygame.image.load('assets/boom.png').convert_alpha()
    bom_list= []
    spawnbom = pygame.USEREVENT+2
    delay_bom=1000
    pygame.time.set_timer(spawnbom, delay_bom)
    bom_height=[50,100,150,200,250]

    pygame.mixer.music.load('sound/nhac.wav')
    pygame.mixer.music.play(-1)

    flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
    hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
    score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
    sfx_swooshing_sound = pygame.mixer.Sound('sound/sfx_swooshing.wav')
    
    gameover=pygame.image.load('assets/gameover.png').convert_alpha()
    gameover=pygame.transform.scale2x(gameover)
    gameover_sunface=gameover.get_rect(center=(400,400))
    
    tamdung=pygame.image.load('assets/pause.jpg').convert()
    tamdung_sunface=tamdung.get_rect(center=(400,400))
    
    floor_top=pygame.image.load('assets/floor-top.png')
    floor_top_sunface=floor_top.get_rect(midleft=(0,-7))
    
    floor_bot=pygame.image.load('assets/floor-bot.png')
    floor_bot_sunface=floor_bot.get_rect(midleft=(0,660))
    
    game_active=False
    pause=True
    bird_alive=False
    bird_alive1=False

    pause_pipe = True
    state=True
    
    while True:
        screen.blit(floor_bot,floor_bot_sunface)
        screen.blit(floor_top,floor_top_sunface)
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 

                    pause_pipe=False
                    state=False
                    pygame.display.flip()
                    pygame.event.pump() 
                    screen.blit(tamdung,tamdung_sunface)
                if event.key == pygame.K_s: 
                    pause_pipe=True
                    state=True
                if state==True :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k and game_active==False:
                            print("k")
                            game_active=True
                            pipe_list.clear()
                            bom_list.clear()
                            
                            bird_alive=True
                            bird_movement=0
                            bird_rect.center=(100,324)
                                
                            bird_alive1=True
                            bird_movement1=0
                            bird_rect1.center=(100,354)
                        # bird 0
                        if event.key == pygame.K_SPACE and game_active and bird_alive:

                            bird_movement=0
                            bird_movement-=2
                            flap_sound.play()
                            sfx_swooshing_sound.play()

                        if event.key == pygame.K_d and game_active and bird_alive:
                            bird_rect.centerx +=100
                        if event.key == pygame.K_a and game_active and bird_alive:
                            bird_rect.centerx -=100
                        # bird 1
                        if event.key == pygame.K_KP_ENTER and game_active and bird_alive1:

                            bird_movement1=0
                            bird_movement1-=2
                            flap_sound.play()
                            sfx_swooshing_sound.play()
                        if event.key == pygame.K_RIGHT and game_active and bird_alive1:
                            bird_rect1.centerx +=100
                        if event.key == pygame.K_LEFT and game_active and bird_alive1:
                            bird_rect1.centerx -=100
            if event.type == spawnpipe and pause_pipe==True:
                
                if a<700:
                    pipe_list.extend(create_pipe())
                    # print("+1 pipe")
                    a=850
            if event.type == spawnbom:
                if b>150:
                   bom_list.append(create_bom())
                   b=-10 
                #    print("+1 bom")
            
            if event.type == birdflap:
                if bird_index < 2:
                    bird_index +=1
                else:
                    bird_index = 0    
                bird, bird_rect, bird1, bird_rect1 = bird_animation()
       
        if pause==False and game_active==False:
            paused()
            pause=True
        elif pause==True and game_active==True:
            unpause()  
            pause=False
        if state==True:
            if game_active:
                # print(pause)
                if pause_pipe==True:    
                    pipe_list = move_pipe(pipe_list)
                    draw_pipe(pipe_list)
                #chim 0
                bird_movement += gravity
                bird_rect.centery += bird_movement
                rotated_bird = rotate_bird(bird)
                screen.blit(rotated_bird,bird_rect)
                #chim1
                bird_movement1 += gravity
                bird_rect1.centery += bird_movement1
                rotated_bird1 = rotate_bird(bird1)
                screen.blit(rotated_bird1,bird_rect1)
                
                # kiểm tra va chạm
                if bird_alive:
                    bird_alive=check_collision(pipe_list,bom_list)
                if bird_alive1:
                    bird_alive1=check_collision1(pipe_list,bom_list)
                if bird_alive==False and bird_alive1==False:
                    delay_dead()
                    game_active=False
                
                
                
                bom_list = move_bom(bom_list)
                draw_bom(bom_list)
                
                if bird_alive:
                    fake_score=len([0 for pipe in pipe_list if pipe.centerx<=bird_rect.centerx])/2
                    if fake_score>score:
                        score_sound.play()
                        score=fake_score
                if bird_alive1:    
                    fake_score=len([0 for pipe in pipe_list if pipe.centerx<=bird_rect1.centerx])/2
                    if fake_score>score1:
                        score_sound.play()
                        score1=fake_score    
                
                score_display('game alive')
                    
            else:
                    
                    # print(pause)
                    screen.blit(message_sunface,message)
                    hight_score=update_score(score,hight_score)
                    score=0
                    score_display('game over')
        else:
            screen.blit(tamdung,tamdung_sunface)
            
        floor_x -=2
        ve_san()
        if floor_x <=-432:
            floor_x=0
            

        pygame.display.update()
        clock.tick(120)

except Exception as e:
    print(e)

input()
    
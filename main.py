from asyncio.windows_events import NULL

try:
    import pygame, sys, random, time,threading   
    from bird import Bird
    from pipe import Pipe
    from bom import Bom
    from bg_floor import BG_FL
    from score_diem import Score
    from sound import *
    def delay_dead():
        screen.blit(gameover,gameover_sunface)
        screen.blit(bg_fl.floor,(bg_fl.floor_x,650))
        screen.blit(bg_fl.floor,(bg_fl.floor_x+672,650)) 
        pygame.event.pump()
        pygame.display.flip()
        pygame.time.delay(1000)
        
    pygame.init()
    screen = pygame.display.set_mode((864,768))
    pygame.display.set_caption("Flappy Bird 2.0")
    clock=pygame.time.Clock()

    gravity = 0.09

    message_sunface = pygame.image.load('assets/message.png').convert_alpha()
    message_sunface = pygame.transform.scale2x(message_sunface)
    message=message_sunface.get_rect(center=(432,374))

    pipe=Pipe(screen)
    bom=Bom(screen)
    bird=Bird(screen,0,'assets/yellowbird-downflap.png','assets/yellowbird-midflap.png','assets/yellowbird-upflap.png')
    bird1=Bird(screen,0,'assets/redbird-downflap.png','assets/redbird-midflap.png','assets/redbird-upflap.png')
    bg_fl = BG_FL(screen)
    score=Score()
    nhacnen(2)

    gameover=pygame.image.load('assets/gameover.png').convert_alpha()
    gameover=pygame.transform.scale2x(gameover)
    gameover_sunface=gameover.get_rect(center=(400,400))

    tamdung=pygame.image.load('assets/pause.png').convert_alpha()
    tamdung_sunface=tamdung.get_rect(center=(400,400))

    game_active=False
    pause_sound=True
    bird_alive=False
    bird_alive1=False

    pause_pipe = True
    state=True

    while True:
        screen.blit(bg_fl.floor_bot,bg_fl.floor_bot_sunface)
        screen.blit(bg_fl.floor_top,bg_fl.floor_top_sunface)
        screen.blit(bg_fl.bg,(0,0))
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
                            game_active=True
                            pipe.pipe_list.clear()
                            bom.bom_list.clear()
                            
                            bird_alive=True
                            bird.start()
                                
                            bird_alive1=True
                            bird1.start()
                        # bird 0
                        if event.key == pygame.K_SPACE and game_active and bird_alive:

                            bird.bird_movement=0
                            bird.bird_movement-=2
                            flap()
                            swooshing()

                        if event.key == pygame.K_d and game_active and bird_alive:
                            bird.bird_rect.centerx +=100
                        if event.key == pygame.K_a and game_active and bird_alive:
                            bird.bird_rect.centerx -=100
                        # bird 1
                        if event.key == pygame.K_KP_ENTER and game_active and bird_alive1:

                            bird1.bird_movement=0
                            bird1.bird_movement-=2
                            
                            flap()
                            swooshing()
                        if event.key == pygame.K_RIGHT and game_active and bird_alive1:
                            bird1.bird_rect.centerx +=100
                        if event.key == pygame.K_LEFT and game_active and bird_alive1:
                            bird1.bird_rect.centerx -=100
            if event.type == pipe.spawnpipe and pause_pipe==True: 
                pipe.add_pipe()
            if event.type == bom.spawnbom and pause_pipe==True:
                bom.add_bom()
            if event.type == bird.birdflap:
                bird.bird_animation()
                bird1.bird_animation()
        
        if pause_sound==False and game_active==False:
            nhacnen(1)
            pause_sound=True
        elif pause_sound==True and game_active==True:
            nhacnen(0)  
            pause_sound=False
        if state==True:
            if game_active:
                # print(pause)
                if pause_pipe==True:
                    pipe.move_pipe()
                    pipe.draw_pipe()
                    bom.move_bom()
                    bom.draw_bom()
            
                bird.fall(gravity)
                bird1.fall(gravity)

                # kiểm tra va chạm
                if bird_alive:
                    bird_alive=bird.check_collision(pipe.pipe_list,bom.bom_list,bg_fl.floor_top_sunface,bg_fl.floor_bot_sunface)
                if bird_alive1:
                    bird_alive1=bird1.check_collision(pipe.pipe_list,bom.bom_list,bg_fl.floor_top_sunface,bg_fl.floor_bot_sunface)
                if bird_alive==False and bird_alive1==False:
                    delay_dead()
                    game_active=False

                if bird_alive:
                    fake_score=len([0 for pipe in pipe.pipe_list if pipe.centerx<=bird.bird_rect.centerx])/2
                    if fake_score>score.score:
                        score_sound()
                        score.score=fake_score
                        
                if bird_alive1:    
                    fake_score=len([0 for pipe in pipe.pipe_list if pipe.centerx<=bird1.bird_rect.centerx])/2
                    if fake_score>score.score1:
                        score_sound()
                        score.score1=fake_score    
                
                score.score_display(screen,'game alive')
            else:
                    screen.blit(message_sunface,message)
                    score.update_score()
                    score.score_display(screen,'game over')
        else:
            screen.blit(tamdung,tamdung_sunface)
            
        bg_fl.move_san()
            
        pygame.display.update()
        clock.tick(120)
except Exception as e:
    print(e)
input()
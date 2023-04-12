from asyncio.windows_events import NULL
try:
    import pygame, sys, random, time,threading   
    from bird import Bird
    from pipe import Pipe
    from bom import Bom
    from bg_floor import BG_FL
    from score_diem import Score
    from trangthai import TT
    from sound import *
    from hoimau import HoiMau

    pygame.init()
    screen = pygame.display.set_mode((864,768))
    pygame.display.set_caption("Flappy Bird 2.0")
    clock=pygame.time.Clock()

    gravity = 0.09
    pipe=Pipe(screen)
    bom=Bom(screen)
    bird=Bird(screen,0,'assets/yellowbird-downflap.png','assets/yellowbird-midflap.png','assets/yellowbird-upflap.png',"yellow")
    bird1=Bird(screen,0,'assets/redbird-downflap.png','assets/redbird-midflap.png','assets/redbird-upflap.png',"red")
    bg_fl = BG_FL(screen)
    hoimau=HoiMau(screen)
    
    quantity_player=1
    score=Score()
    
    tt=TT(screen)
    nhacnen(2)

    game_active=False
    pause_sound=True

    pause = False
    
    state=True
    mau=0
    mau1=0

    while True:  
        mau +=1
        mau1 +=1
        screen.blit(bg_fl.floor_bot,bg_fl.floor_bot_sunface)
        screen.blit(bg_fl.floor_top,bg_fl.floor_top_sunface)
        screen.blit(bg_fl.bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and game_active == False:
                    if quantity_player == 1:
                        quantity_player=2
                    else:
                        quantity_player=1
                if event.key == pygame.K_p: 
                    if pause == False:
                        pause = True
                        bom.pause = False
                        pipe.pause = False
                        hoimau.pause = False
                        state=False
                        pygame.display.flip()
                        pygame.event.pump() 
                        screen.blit(tt.tamdung,tt.tamdung_sunface)
                    else:
                        pause = False
                        bom.pause=True
                        pipe.pause=True
                        hoimau.pause=True
                        state=True
                if state==True :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k and game_active==False:
                            game_active=True
                            pipe.pipe_list.clear()
                            bom.bom_list.clear()
                            hoimau.mau_list.clear()
                            bird.start()
                            if quantity_player == 2:
                                bird1.start()
                        # bird 0
                        if event.key == pygame.K_SPACE and game_active and bird.mau:

                            bird.bird_movement=0
                            bird.bird_movement-=3
                            flap()
                            swooshing()

                        if event.key == pygame.K_d and game_active and bird.mau:
                            bird.bird_rect.centerx +=100
                        if event.key == pygame.K_a and game_active and bird.mau:
                            bird.bird_rect.centerx -=100
                        # bird 1
                        if event.key == pygame.K_KP_ENTER and game_active and bird1.mau and quantity_player==2:

                            bird1.bird_movement=0
                            bird1.bird_movement-=3
                            
                            flap()
                            swooshing()
                        if event.key == pygame.K_RIGHT and game_active and bird1.mau and quantity_player==2:
                            bird1.bird_rect.centerx +=100
                        if event.key == pygame.K_LEFT and game_active and bird1.mau and quantity_player==2:
                            bird1.bird_rect.centerx -=100
            if event.type == bird.birdflap:
                bird.bird_animation()
                if quantity_player ==2:
                    bird1.bird_animation()
        bom.add_bom()        
        pipe.add_pipe()
        hoimau.add_mau()
        if pause_sound==False and game_active==False:
            nhacnen(1)
            pause_sound=True
        elif pause_sound==True and game_active==True:
            nhacnen(0)  
            pause_sound=False
        if state==True:
            if game_active:
                
                pipe.move_pipe()
                pipe.draw_pipe()                
                
                hoimau.move_mau()
                hoimau.draw_mau()
                
                pipe.update_pipe(score.score if score.score>score.score1 else score.score1)
                
                bom.move_bom()
                bom.draw_bom()
                            
                bird.fall(gravity)
                if quantity_player ==2:
                    bird1.fall(gravity)
                
                bird.hoimau(hoimau.mau_list)
                if quantity_player ==2: 
                    bird1.hoimau(hoimau.mau_list)

                # kiểm tra va chạm
                if bird.mau>0:  
                    alive=bird.check_collision(pipe.pipe_list,bom.bom_list,bg_fl.floor_top_sunface,bg_fl.floor_bot_sunface)
                    if mau>=120 and alive==False:
                        mau=0
                        bird.mau-=1
                if quantity_player ==2:
                    if bird1.mau>0:  
                        alive=bird1.check_collision(pipe.pipe_list,bom.bom_list,bg_fl.floor_top_sunface,bg_fl.floor_bot_sunface)
                        if mau1>=120 and alive==False:
                            mau1=0
                            bird1.mau-=1
                if quantity_player ==2:        
                    if bird.mau==0 and bird1.mau==0:
                        tt.delay_dead(bg_fl)
                        game_active=False
                else:
                    if bird.mau==0:
                        tt.delay_dead(bg_fl)
                        game_active=False

                if bird.mau:
                    fake_score=len([0 for pipe in pipe.pipe_list if pipe.centerx<=bird.bird_rect.centerx])/2
                    if fake_score>score.score:
                        score_sound()
                        score.score=fake_score
                
                if quantity_player ==2:        
                    if bird1.mau:    
                        fake_score=len([0 for pipe in pipe.pipe_list if pipe.centerx<=bird1.bird_rect.centerx])/2
                        if fake_score>score.score1:
                            score_sound()
                            score.score1=fake_score    
                
                score.score_display(screen,'game alive',quantity_player)
            else:
                    screen.blit(tt.message_sunface,tt.message)
                    tt.number_player(quantity_player)
                    score.update_score(quantity_player)
                    score.score_display(screen,'game over',quantity_player)
        else:
            screen.blit(tt.tamdung,tt.tamdung_sunface)
            
        bg_fl.move_san()
            
        pygame.display.update()
        clock.tick(120)
except Exception as e:
    print(e)
input()
try:


	import pygame
	import sys
	import random
	from random import randint
	from pygame import mixer

	def gameplay():
	#thiết lập dữ liệu:
		count = 0
		over = False
		speed = 3
		
		#background
		background_x = 0
		ground_x = 0

		background = pygame.image.load('background\\background.png')
		background = pygame.transform.scale(background , (800,330))

		ground = pygame.image.load('background\\ground.png')
		ground = pygame.transform.scale(ground , (800,70))

		#player
		player_x = 400
		player_y = 290
		move_right = False
		move_left = False
		jump = False
		teleport = False
		flash = 150

		player1 = pygame.image.load('player\\herochar_run_0.png')
		player1 = pygame.transform.scale(player1 , (40,40))
		player2 = pygame.image.load('player\\herochar_run_1.png')
		player2 = pygame.transform.scale(player2 , (40,40))
		player3 = pygame.image.load('player\\herochar_run_2.png')
		player3 = pygame.transform.scale(player3 , (40,40))
		player4 = pygame.image.load('player\\herochar_run_3.png')
		player4 = pygame.transform.scale(player4 , (40,40))
		player5 = pygame.image.load('player\\herochar_run_4.png')
		player5 = pygame.transform.scale(player5 , (40,40))
		player6 = pygame.image.load('player\\herochar_run_5.png')
		player6 = pygame.transform.scale(player6 , (40,40))

		player7 = pygame.image.load('player\\herochar_jump_up.png')
		player7 = pygame.transform.scale(player7 , (40,40))
		player8 = pygame.image.load('player\\herochar_jump_down.png')
		player8 = pygame.transform.scale(player8 , (40,40))

		listplayer = [player1,player2,player3,player4,player5,player6,player7,player8]

		#monster
		monster1_x = 800
		monster2_x = 800+600
		monster1_y = 272
		monster2_y = 272

		goblin1 = pygame.image.load('Goblin\\Run1.png')
		goblin1 = pygame.transform.scale(goblin1 , (45,60))
		goblin2 = pygame.image.load('Goblin\\Run2.png')
		goblin2 = pygame.transform.scale(goblin2 , (45,60))
		goblin3 = pygame.image.load('Goblin\\Run3.png')
		goblin3 = pygame.transform.scale(goblin3 , (45,60))
		goblin4 = pygame.image.load('Goblin\\Run4.png')
		goblin4 = pygame.transform.scale(goblin4 , (45,60))
		goblin5 = pygame.image.load('Goblin\\Run5.png')
		goblin5 = pygame.transform.scale(goblin5 , (45,60))
		goblin6 = pygame.image.load('Goblin\\Run6.png')
		goblin6 = pygame.transform.scale(goblin6 , (45,60))
		goblin7 = pygame.image.load('Goblin\\Run7.png')
		goblin7 = pygame.transform.scale(goblin7 , (45,60))
		goblin8 = pygame.image.load('Goblin\\Run8.png')
		goblin8 = pygame.transform.scale(goblin8 , (45,60))

		listgoblin = [goblin1,goblin2,goblin3,goblin4,goblin5,goblin6,goblin7,goblin8]

		mushroom1 = pygame.image.load('Mushroom\\Run1.png')
		mushroom1 = pygame.transform.scale(mushroom1 , (45,60))
		mushroom2 = pygame.image.load('Mushroom\\Run2.png')
		mushroom2 = pygame.transform.scale(mushroom2 , (45,60))
		mushroom3 = pygame.image.load('Mushroom\\Run3.png')
		mushroom3 = pygame.transform.scale(mushroom3 , (45,60))
		mushroom4 = pygame.image.load('Mushroom\\Run4.png')
		mushroom4 = pygame.transform.scale(mushroom4 , (45,60))
		mushroom5 = pygame.image.load('Mushroom\\Run5.png')
		mushroom5 = pygame.transform.scale(mushroom5 , (45,60))
		mushroom6 = pygame.image.load('Mushroom\\Run6.png')
		mushroom6 = pygame.transform.scale(mushroom6 , (45,60))
		mushroom7 = pygame.image.load('Mushroom\\Run7.png')
		mushroom7 = pygame.transform.scale(mushroom7 , (45,60))
		mushroom8 = pygame.image.load('Mushroom\\Run8.png')
		mushroom8 = pygame.transform.scale(mushroom8 , (45,60))

		listmushroom = [mushroom1,mushroom2,mushroom3,mushroom4,mushroom5,mushroom6,mushroom7,mushroom8]

		listmonster = [listmushroom,listgoblin]

		#fire
		fire_x = 0
		fire_y = 0
		fire2_x = 0
		fire2_y = -133
		fire3_x = 0
		fire3_y = -266

		fire = pygame.image.load('fire\\lua1.png')
		fire = pygame.transform.scale(fire , (30,30))

		#item
		x = 800
		y = 150
		move_item = 'up'
		status = True
		energy = 3
		health = 3

		energy_item = pygame.image.load('item\\energy.png') 
		energy_item = pygame.transform.scale(energy_item , (15,20))
		health_item = pygame.image.load('item\\health.png')
		health_item = pygame.transform.scale(health_item , (15,20))

		items = [energy_item,health_item]

		#score & level
		diem = 0
		plus_diem = 1
		level = 0
		
		#text
		font_big = pygame.font.SysFont('san' , 50)
		font_small = pygame.font.SysFont('san',30)
		overtext = font_big.render('Game over', True, (255,0,0) )
		smalltext_play = font_small.render('Retry' , True , (255,255,255))
		smalltext_menu = font_small.render('Menu' , True , (255,255,255))

		#màu nút
		color_light = (170,170,170)
		color_dark = (100,100,100)

		#sound
		soundJ = pygame.mixer.Sound('Sounds\\Jump.mp3')
		soundL = pygame.mixer.Sound('Sounds\\Lose.mp3')
		soundT = pygame.mixer.Sound('Sounds\\teleport.wav')
		SoundBC = pygame.mixer.Sound('Sounds\\button_click.wav')

		#music
		mixer.music.load('Sounds\\music.mp3')
		mixer.music.play(-1) #(-1) phát nhạc liên tục 

	# main game (loop)
		while True:
			clock.tick(60)
			mouse = pygame.mouse.get_pos()
			count += 1

		#background
			background_x -= 1
			if background_x <= -800:
				background_x = 0	

			ground_x -= speed
			if ground_x <= -800:
				ground_x = 0

		#player
			#animation:
			if player_y ==290 :
				if count%30 > 0 and count%30 <=5:
					i = 0
				elif count%30 > 5 and count%30 <=10:
					i = 1
				elif count%30 > 10 and count%30 <=15:
					i =2
				elif count%30 > 15 and count%30 <=20:
					i = 3
				elif count%30 > 20 and count%30 <=25:
					i =4
				else:
					i = 5
			else:
				if player_y < 290 and jump == True:
					i = 6
				else:
					i =7	
			#di chuyển
			if player_x > 755: 
				move_right = False	
			if move_right == True:
				player_x += speed

			if player_x < 0:
				move_left = False
			if move_left == True:
				player_x -= speed
			#nhảy
			if 150 <= player_y <= 290 and jump == True:
				player_y -= speed
			else:
				jump = False
			if  player_y < 290 and jump == False:
				player_y += speed
			#skill
			if teleport == True:
				pygame.mixer.Sound.play(soundT)
				if 755 - player_x <= flash:
					flash = 755 - player_x
				else:
					flash = 150
				player_x += flash
				teleport = False

		#monster
			if count%40 > 0 and count%40 <= 5:
				j = 0
			elif count%40 > 5 and count%40 <= 10:
				j = 1
			elif count%40 > 10 and count%40 <= 15:
				j = 2
			elif count%40 > 15 and count%40 <= 20:
				j = 3
			elif count%40 > 20 and count%40 <= 25:
				j = 4
			elif count%40 > 25 and count%40 <= 30:
				j = 5
			elif count%40 > 30 and count%40 <= 35:
				j = 6
			else:
				j = 7

			if monster1_x == 800 or monster1_x == 1200:
				monstert1 = random.choice(listmonster)	# random monster
			
			if monster2_x == 1200 or monster2_x == 800+600:
				monstert2 = random.choice(listmonster)

			monster1_x -= (speed+level+1)
			monster2_x -= (speed+level+1)
			if monster1_x < -60:
				monster1_x = 1200
				monster1_y = 272
			if monster2_x < -60:
				monster2_x = 1200
				monster2_y = 272	

		#fire
			if fire_y <= 0: 
				fire_x = randint(50,800)# random vi trí xuất hiện

			if fire2_y <= 0:
				fire2_x = randint(50,800)

			if fire3_y <= 0:
				fire3_x = randint(50,800)

			fire_y += (speed+level)
			fire_x -= speed
			fire2_y += (speed+level)
			fire2_x -=speed
			fire3_y += (speed+level)
			fire3_x -=speed
			
			if fire_y  >= 400 :
				fire_y = 0
				fire_x = 0

			if fire2_y >= 400:
				fire2_x = 0
				fire2_y = 0

			if fire3_y >= 400:
				fire3_x = 0
				fire3_y = 0

		#item
			if x == 800:
				item = random.choice(items) #lựa chọn loại item
			x -= 2
			if x<0:
			    status = True #hiện item
			    x = 800
			#di chuyển lên xuống
			if y >= 250:
			    move_item = 'down'
			if y <= 150:
			    move_item = 'up'

			if move_item == 'up':
			    y += 1
			else :
			    y -= 1

		#va chạm
			vacham1 = collision(listplayer[i], (player_x , player_y), monstert1[j], (monster1_x  , monster1_y))
			vacham2 = collision(listplayer[i], (player_x , player_y), monstert2[j], (monster2_x  , monster2_y))
			vacham3 = collision(listplayer[i], (player_x , player_y), fire, (fire_x , fire_y))
			vacham4 = collision(listplayer[i], (player_x , player_y), fire, (fire2_x , fire2_y))
			vacham5 = collision(listplayer[i], (player_x , player_y), fire, (fire3_x , fire3_y))
			vacham6 = collision(listplayer[i], (player_x , player_y), energy_item, (x  , y))
			#dụng quái vật
			if vacham1 or vacham2:
				health -=1
				if over == False:
					pygame.mixer.Sound.play(soundL)#phát âm thanh
				if vacham1:
					monster1_y = -60
				else:
					monster2_y = -60
			#đụng lửa
			if  vacham3 or vacham4 or vacham5 :	
				health -=1
				if over == False:
					pygame.mixer.Sound.play(soundL)#phát âm thanh
				if vacham3:
					fire_x = 0
				elif vacham4:
					fire2_x = 0
				else:
					fire3_x = 0
			#hết máu -> thua
			if health == 0 :
				over = True
				mixer.music.stop()
			#dụng item
			if vacham6 :
				pygame.mixer.Sound.play(SoundBC)
				status = False
				if item == energy_item and energy < 5:
					energy +=1
				if item == health_item and health < 5:
					health +=1
				x -= flash

		#điểm, độ khó
			if count%60 == 0:
				diem += plus_diem
				if diem%10 == 0 and level <= 3:
					level += 1
			diem_txt = font_small.render("score : " + str(diem), True, (255,0,0))
			
		#vẽ
			background_rect = screen.blit(background , (background_x , 0))
			background_rect_1 = screen.blit(background , (background_x+800 , 0))

			fire_rect1 = screen.blit(fire , (fire_x , fire_y))
			fire_rect2 = screen.blit(fire , (fire2_x , fire2_y))
			fire_rect3 = screen.blit(fire , (fire3_x , fire3_y))

			ground_rect1 = screen.blit(ground , (ground_x , 330))
			ground_rect11 = screen.blit(ground , (ground_x + 800 , 330))

			monster1_rect = screen.blit(monstert1[j] , (monster1_x  , monster1_y))
			monster2_rect = screen.blit(monstert2[j] , (monster2_x  , monster2_y))

			diem_rect = screen.blit(diem_txt, (5,5) )

			if status == True:    
			    screen.blit(item , (x, y))

			for e in range(energy):
			    screen.blit(energy_item , (700+e*20, 10))
			for h in range(health):
				screen.blit(health_item, (700+h*20, 35))

			if over == False:
				player = screen.blit(listplayer[i] , (player_x , player_y))
			else:
				plus_diem = 0
				energy = 0
				player_y = 400
				screen.blit(overtext, (315,150))
				if (230 <= mouse[0] <= 370) and (200 <= mouse[1] <= 240):
					pygame.draw.rect(screen,color_light,[230,200,140,40])
					screen.blit(smalltext_play , (277,210))
				elif (430 <= mouse[0] <= 570) and (200 <= mouse[1] <= 240):
					pygame.draw.rect(screen,color_light,[430,200,140,40])
					screen.blit(smalltext_menu , (477,210))
				else:
					pygame.draw.rect(screen,color_dark,[230,200,140,40])
					pygame.draw.rect(screen,color_dark,[430,200,140,40])
					screen.blit(smalltext_play , (277,210))
					screen.blit(smalltext_menu , (477,210))

		#bắt sự kiện tay
			for event in pygame.event.get(): 
				#thoát
				if event.type == pygame.QUIT: 
					pygame.quit()
					sys.exit()
				#nhấn phím
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE: 
						if player_y == 290: 
							jump = True
							pygame.mixer.Sound.play(soundJ)
					if event.key == pygame.K_RIGHT:
						move_right = True
					if event.key == pygame.K_LEFT:
						move_left = True
					if event.key == pygame.K_UP:
						if energy > 0:
							teleport = True
							energy -=1
				#thả phím
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						move_right = False
					if event.key == pygame.K_LEFT:
						move_left = False
				#nhấn chuột
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]: #click trái
						if over == True:
							if (230 <= mouse[0] <= 370) and (200 <= mouse[1] <= 240):
								pygame.mixer.Sound.play(SoundBC)
								mixer.music.play(-1)
								count = 0
								player_x = 400
								player_y = 290
								monster1_x = 800
								monster2_x = 800+600
								fire_y = 0
								fire2_y = -133
								fire3_y = -266
								diem = 0
								plus_diem = 1
								level = 0
								jump = False
								energy = 3
								health = 3
								status = True
								x = 800
								over = False
							if (430 <= mouse[0] <= 570) and (200 <= mouse[1] <= 240):
								pygame.mixer.Sound.play(SoundBC)
								menu()

			pygame.display.update()

	def menu():
		count = 0
		
		background_x = 0
		ground_x = 0
		background = pygame.image.load('background\\background.png')
		background = pygame.transform.scale(background , (800,330))
		ground = pygame.image.load('background\\ground.png')
		ground = pygame.transform.scale(ground , (800,70))

		player1 = pygame.image.load('player\\herochar_run_0.png')
		player1 = pygame.transform.scale(player1 , (40,40))
		player2 = pygame.image.load('player\\herochar_run_1.png')
		player2 = pygame.transform.scale(player2 , (40,40))
		player3 = pygame.image.load('player\\herochar_run_2.png')
		player3 = pygame.transform.scale(player3 , (40,40))
		player4 = pygame.image.load('player\\herochar_run_3.png')
		player4 = pygame.transform.scale(player4 , (40,40))
		player5 = pygame.image.load('player\\herochar_run_4.png')
		player5 = pygame.transform.scale(player5 , (40,40))
		player6 = pygame.image.load('player\\herochar_run_5.png')
		player6 = pygame.transform.scale(player6 , (40,40))
		listplayer = [player1,player2,player3,player4,player5,player6]

		font_big = pygame.font.SysFont('Blackadder ITC' , 50)
		bigtext = font_big.render("Run Run ", True, (255,0,0) )

		font_small = pygame.font.SysFont('Blackadder ITC',30)
		smalltext = font_small.render('play' , True , (255,255,255))
		  
		color_light = (170,170,170)
		color_dark = (100,100,100)

		SoundBC = pygame.mixer.Sound('Sounds\\button_click.wav')
		  
		width = screen.get_width()
		  
		height = screen.get_height()

		while True:
			clock.tick(60)
			count +=1
			
			background_rect = screen.blit(background , (background_x,0))
			background_rect1 = screen.blit(background , (background_x+800,0))
			ground_rect = screen.blit(ground , (ground_x,330))
			ground_rect1 = screen.blit(ground , (ground_x+800,330))

			background_x -= 1
			if background_x <= -800:
				background_x = 0	

			ground_x -= 2
			if ground_x <= -800:
				ground_x = 0

			#player
			if count%30 > 0 and count%30 <=5:
				i = 0
			elif count%30 > 5 and count%30 <=10:
				i = 1
			elif count%30 > 10 and count%30 <=15:
				i = 2
			elif count%30 > 15 and count%30 <=10:
				i = 3
			elif count%30 > 20 and count%30 <=25:
				i = 4
			else:
				i = 5            
		      
			mouse = pygame.mouse.get_pos()
		    
			if ( (width-140)/2 <= mouse[0] <= (width-140)/2+140 ) and ( height/2 <= mouse[1] <= height/2+40 ):
				pygame.draw.rect(screen,color_light,[(width-140)/2,height/2,140,40])
			else:
				pygame.draw.rect(screen,color_dark,[(width-140)/2,height/2,140,40])

			for ev in pygame.event.get():   
				if ev.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		        #kiễm tra click chuột
				if ev.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]: #click chuột trái
						if ((width-140)/2 <= mouse[0] <= (width-140)/2+140) and (height/2 <= mouse[1] <= height/2+40):
							pygame.mixer.Sound.play(SoundBC)
							gameplay()

			screen.blit(smalltext,((width-50)/2,height/2))
			pygame.draw.circle(screen,(255,210,210),((width/2+85+15,height/2-55+20)),25)
			screen.blit(listplayer[i],(width/2+80,height/2-55))
			screen.blit(bigtext,(width/2-110,height/2-70))

			pygame.display.update()

	def collision(surface1, pos1, surface2, pos2):
	    mask1 = pygame.mask.from_surface(surface1)
	    mask2 = pygame.mask.from_surface(surface2)
	    x = pos2[0] - pos1[0]
	    y = pos2[1] - pos1[1]
	    if mask1.overlap(mask2,(x, y)) != None:
	        return True
	    return False
	    
	pygame.init()

	screen = pygame.display.set_mode((800,400))

	pygame.display.set_caption('RUNRUN')

	clock = pygame.time.Clock()

	menu()



except Exception as e:
	print(e)


input()
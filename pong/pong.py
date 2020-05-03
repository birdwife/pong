import pygame
from paddle import HappyAdriana
from paddle import HappyNicole
from paddle import SadAdriana
from paddle import SadNicole
from ball import Ball

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

size = (700,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("NICOLES PONG GAME :)")
 
adri1 = HappyAdriana(GREEN,100,100)
adri1.rect.x = 20
adri1.rect.y = 320
nicole1 = HappyNicole(GREEN,100,100)
nicole1.rect.x = 580
nicole1.rect.y = 320
ball1 = Ball(GREEN,50,50)
ball1.rect.x = 10
ball1.rect.y = 10

allSpritesList = pygame.sprite.Group()
allSpritesList.add(adri1)
allSpritesList.add(nicole1)
allSpritesList.add(ball1)

adriScore = 0
nicoleScore = 0

switch = True

clock = pygame.time.Clock()

while switch:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			switch = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				switch = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		nicole1.moveUp(10)
	if keys[pygame.K_DOWN]:
		nicole1.moveDown(10)
	if keys[pygame.K_LEFT]:
		nicole1.moveLeft(10)
	if keys[pygame.K_RIGHT]:
		nicole1.moveRight(10)
	if keys[pygame.K_w]:
		adri1.moveUp(10)
	if keys[pygame.K_s]:
		adri1.moveDown(10)
	if keys[pygame.K_a]:
		adri1.moveLeft(10)
	if keys[pygame.K_d]:
		adri1.moveRight(10)

	allSpritesList.update()

	if ball1.rect.x > 650:
		ball1.rect.x = 350
		ball1.rect.y = 350
		ball1.bounce()
		adriScore += 1
		allSpritesList.update()

	if ball1.rect.x < 0:
		ball1.rect.x = 350
		ball1.rect.y = 350
		ball1.bounce()
		nicoleScore += 1
		allSpritesList.update()
 
	if ball1.rect.y > 650:
		ball1.rect.y = 350
		ball1.rect.x = 350
		ball1.bounce()
		allSpritesList.update()
		if ball1.rect.x < 350:
			nicoleScore += 1
		if ball1.rect.x > 350:
			adriScore += 1

	if ball1.rect.y < 0:
		ball1.rect.y = 350
		ball1.rect.x = 350
		ball1.bounce()
		allSpritesList.update()
		if ball1.rect.x < 350:
			nicoleScore += 1
		if ball1.rect.x > 350:	
			adriScore += 1

	if nicole1.rect.x < 355 :
		nicole1.rect.x = 355
	if adri1.rect.x > 245 :
		adri1.rect.x = 245
	
	if pygame.sprite.collide_mask(ball1, adri1) or pygame.sprite.collide_mask(ball1, nicole1):
		ball1.bounce()
	
	if pygame.sprite.collide_mask(ball1, nicole1):
		pos1 = nicole1.rect.x
		pos2 = nicole1.rect.y
		allSpritesList.remove(nicole1)
		nicole1 = SadNicole(GREEN, 100, 100)
		nicole1.rect.x = pos1
		nicole1.rect.y = pos2
		allSpritesList.add(nicole1)
		allSpritesList.update()
		allSpritesList.draw(screen)

	if ball1.rect.x < 550:
		pos1 = nicole1.rect.x
		pos2 = nicole1.rect.y
		allSpritesList.remove(nicole1)
		nicole1 = HappyNicole(GREEN, 100, 100)
		nicole1.rect.x = pos1
		nicole1.rect.y = pos2
		allSpritesList.add(nicole1)
		allSpritesList.update()
		allSpritesList.draw(screen)
	
	if pygame.sprite.collide_mask(ball1, adri1):
		pos3 = adri1.rect.x
		pos4 = adri1.rect.y
		allSpritesList.remove(adri1)
		adri1 = SadAdriana(GREEN, 100, 100)
		adri1.rect.x = pos3
		adri1.rect.y = pos4
		allSpritesList.add(adri1)
		allSpritesList.update()
		allSpritesList.draw(screen)

	if ball1.rect.x > 200:
		pos3 = adri1.rect.x
		pos4 = adri1.rect.y
		allSpritesList.remove(adri1)
		adri1 = HappyAdriana(GREEN, 100, 100)
		adri1.rect.x = pos3
		adri1.rect.y = pos4
		allSpritesList.add(adri1)
		allSpritesList.update()
		allSpritesList.draw(screen) 
		
	screen.fill(BLACK)
	pygame.draw.line(screen, GREEN, [349,0], [349, 700], 5)
	allSpritesList.draw(screen)

	font = pygame.font.Font(None, 74)
	text = font.render(str(adriScore), 1, GREEN)
	screen.blit(text, (160,0))

	font = pygame.font.Font(None, 74)
	text = font.render(str(nicoleScore), 1, GREEN)
	screen.blit(text, (510, 0))


	pygame.display.flip()
	clock.tick(60)

pygame.quit()

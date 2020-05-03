import pygame
BLACK = (0,0,0)

class HappyAdriana(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()

		self.pic = pygame.image.load('adriana1.png').convert_alpha()
		self.image.blit(self.pic,[0,0])

	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		test = self.rect.y + pixels
		if test > 610:
			self.rect.y = 610
		if test < 610:
			self.rect.y = test

	def moveLeft(self, pixels):
		test = self.rect.x - pixels
		if test < 0 :
			self.rect.x = 0
		if test > 0 :
			self.rect.x = test

	def moveRight(self, pixels):
		test = self.rect.x + pixels
		if test > 610 :
			self.rect.x = 610
		if test < 610 :
			self.rect.x = test
		

class HappyNicole(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()

		self.pic = pygame.image.load('nicole1.png').convert_alpha()
		self.image.blit(self.pic,[0,0])

	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		test = self.rect.y + pixels
		if test > 610:
			self.rect.y = 610
		if test < 610:
			self.rect.y = test

	def moveLeft(self, pixels):
		test = self.rect.x - pixels
		if test < 0 :
			self.rect.x = 0
		if test > 0 :
			self.rect.x = test

	def moveRight(self, pixels):
		test = self.rect.x + pixels
		if test > 610 :
			self.rect.x = 610
		if test < 610 :
			self.rect.x = test


class SadAdriana(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()
				
		self.pic = pygame.image.load('adriana2.png').convert_alpha()
		self.image.blit(self.pic,[0,0])

	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		test = self.rect.y + pixels
		if test > 610:
			self.rect.y = 610
		if test < 610:
			self.rect.y = test

	def moveLeft(self, pixels):
		test = self.rect.x - pixels
		if test < 0 :
			self.rect.x = 0
		if test > 0 :
			self.rect.x = test
	
	def moveRight(self, pixels):
		test = self.rect.x + pixels
		if test > 610 :
			self.rect.x = 610
		if test < 610 :
			self.rect.x = test



class SadNicole(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()

		self.pic = pygame.image.load('nicole2.png').convert_alpha()
		self.image.blit(self.pic,[0,0])
	
	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		test = self.rect.y + pixels
		if test > 610:
			self.rect.y = 610
		if test < 610:
			self.rect.y = test

	def moveLeft(self, pixels):
		test = self.rect.x - pixels
		if test < 0 :
			self.rect.x = 0
		if test > 0 :
			self.rect.x = test

	def moveRight(self, pixels):
		test = self.rect.x + pixels
		if test > 610 :
			self.rect.x = 610
		if test < 610 :
			self.rect.x = test




		

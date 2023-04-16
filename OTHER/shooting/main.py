import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock  = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
y = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	y = y + 1
	if (y > 200):
		y = 0

# místo pro vykreslení
	screen.blit(wood_bg,(0,0))
	screen.blit(land_bg,(0,560 - y))



	pygame.display.update()
	clock.tick(120)

import pygame

print("starting")
pygame.init()
print("pygame init ok")
screen = pygame.display.set_mode((400, 300))
print("window created")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print("done")

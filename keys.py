import sys, pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Keys test")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key, pygame.key.name(event.key))
    pygame.display.flip()
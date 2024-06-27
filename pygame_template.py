import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Planetary Orbit Simulation")
screen = pygame.display.set_mode((1500, 900), pygame.RESIZABLE)
clock = pygame.time.Clock()
screen.fill("black")

# global constants


def update_display(screen):
    screen.fill("black")
    pygame.display.flip()


# variables
running = True
started = False

while running:

    clock.tick(80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
            
            elif event.key == pygame.K_DELETE or event.key == pygame.K_x:
                pass

            elif (event.key == pygame.K_RETURN or event.key == pygame.K_s) and not started:
                started = True

    update_display(screen)
pygame.quit()
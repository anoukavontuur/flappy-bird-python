import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
running = True

#images
flappy_bird_image = pygame.image.load("flappybird.png").convert_alpha()
flappy_bird_image = pygame.transform.scale(flappy_bird_image, 
                                           (flappy_bird_image.get_width() /6, 
                                            flappy_bird_image.get_height()/6))

flappy_pos_x = 0
flappy_pos_y = 400

while running:
    screen.fill((255, 255, 255)) #white background

    screen.blit(flappy_bird_image, (flappy_pos_x, flappy_pos_y))
    flappy_pos_y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappy_pos_y -= 30


    # screen.fill((255, 255, 255)) #white background
    pygame.display.flip() #update the display
    clock.tick(60) 

pygame.quit()
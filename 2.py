import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

songs = ['BigPoppa.mp3', 'Freedom.mp3', 'ShapeOfYou.mp3', 'Sunflower.mp3', 'Flower.mp3']
i = 0
pygame.mixer.music.load(songs[0])

font = pygame.font.Font(None, 72)
pygame.mixer.music.set_volume(0.5)

done = False
playing = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.play()
        playing = True
    if pressed[pygame.K_DOWN]: 
        pygame.mixer.music.stop()
        playing = False
    if pressed[pygame.K_LEFT]: 
        i = (i + 4) % 5
        pygame.mixer.music.load(songs[i])
        if playing: pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]: 
        i = (i + 1) % 5
        pygame.mixer.music.load(songs[i])
        if playing: pygame.mixer.music.play()

    pygame.mixer.music.set_volume(0.1)
    if playing: text = font.render("Currently playing: " + songs[i], True, (100, 100, 200))
    else: text = font.render("Currently NOT playing: " + songs[i], True, (100, 100, 200))
    screen.fill((255, 255, 255))
    screen.blit(text, (500 - text.get_width() // 2, 250 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(15)


    
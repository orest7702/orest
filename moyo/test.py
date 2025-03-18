import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 394))
win = pygame.image.load('../foto/pixil-frame-0 (10).png')
window = [pygame.image.load('../ryh/stop_ryh.png')]
bloc = pygame.image.load('../foto/block.png')

win_x = 0

left = [
    pygame.image.load('../ryh/left/left_1.png'),
    pygame.image.load('../ryh/left/left_2.png'),
    pygame.image.load('../ryh/left/left_3.png'),
    pygame.image.load('../ryh/left/left_4.png'),
]
right = [
    pygame.image.load('../ryh/right/right_1.png'),
    pygame.image.load('../ryh/right/right_2.png'),
    pygame.image.load('../ryh/right/right_3.png'),
    pygame.image.load('../ryh/right/right_4.png'),
]

animals = 0
jump = False
ss = 200
plaer_y = 300
plaer_x = 200
uu = window
ese = True
blok_x = 0

right_right = left_left = False

while ese:

    if uu == window:
        animals = 0

    elif animals >= 4:
        animals = 0

    elif win_x >= 600:
        win_x = 0

    elif win_x <= 0:
        win_x = 600

    screen.blit(win, (win_x - 700, 0))
    screen.blit(win, (win_x, 0))
    screen.blit(win, (win_x + 700, 0))
    screen.blit(bloc, (win_x - 700, 250))
    screen.blit(bloc, (win_x, 250))
    screen.blit(bloc, (win_x + 800, 250))

    clock.tick(10)
    screen.blit(uu[animals], (plaer_x, plaer_y))

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            ese = False
            pygame.quit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                left_left = True

            elif i.key == pygame.K_RIGHT:
                right_right = True

            elif i.key == pygame.K_SPACE:
                jump = True

        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT or i.key == pygame.K_SPACE:
                uu = window
                left_left = right_right = False

    if left_left:
        win_x += 10
        uu = left
        animals += 1

    if right_right:
        win_x -= 10
        uu = right
        animals += 1

    if jump:
        a = 300 - ss
        s = a / 10
        plaer_y -= s

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 700))

R = []
for _ in range(1):
    for q in range(0, 700, 70):
        for w in range(0, 700, 70):
            r_r = pygame.Rect(q, w, 69, 69)
            R.append(r_r)

green = (0, 250, 0)
blue = (0, 0, 250)


def quit_quit():
    pygame.quit()
    sys.exit()


for i in range(100):
    pygame.draw.rect(screen, blue, R[i], 0)
while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rr in R:
                if rr.collidepoint(pos):
                    color = green
                    pygame.draw.rect(screen, color, rr, 0)

    pygame.display.flip()

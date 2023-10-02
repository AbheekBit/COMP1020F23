import pygame, sys, math


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))

    ball = pygame.image.load("GolfBall.png").convert_alpha()
    ball_rect = ball.get_rect()

    wizard = pygame.image.load("pixel-art.gif").convert_alpha()
    wizard_rect = wizard.get_rect()

    is_playing = True
    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pos = pygame.mouse.get_pos()
        ball_rect.center = pos

        screen.fill((0, 0, 0))
        ball_rect.move_ip(20, 10)
        screen.blit(ball, ball_rect)
        screen.blit()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

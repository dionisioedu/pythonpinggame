import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCORE_POS_X = 20
SCORE_POS_Y = 20


UP_RIGHT = 0
DOWN_RIGHT = 1
UP_LEFT = 2
DOWN_LEFT = 3

BALL_SPEED = 5.0

BALL_INITIAL_X = 380
BALL_INITIAL_Y = 280

BALL_WIDTH = 40
BALL_HEIGHT = 40

RACKET_WIDTH = 120

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong")
    pygame.display.flip()

    background = pygame.image.load('images/background.png').convert()
    racket = pygame.image.load('images/racket.png').convert()
    ball = pygame.image.load('images/ball.png')
    life = pygame.image.load('images/life.png')
    gameover = pygame.image.load('images/gameover.png')

    ball_direction = UP_RIGHT
    ball_x = BALL_INITIAL_X
    ball_y = BALL_INITIAL_Y
    ball_speed = BALL_SPEED

    racket_x = 340
    racket_y = 580

    lifes = 3

    InGame = True
    Playing = True
    while Playing:
        pygame.time.wait(20)

        #Check if ball hit racket
        if ((ball_x + BALL_WIDTH) >= racket_x) and (ball_x < (racket_x + RACKET_WIDTH)) and ((ball_y + BALL_HEIGHT) >= racket_y):
            if ball_direction == DOWN_LEFT:
                ball_direction = UP_LEFT
            elif ball_direction == DOWN_RIGHT:
                ball_direction = UP_RIGHT

            ball_speed += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Playing = False
            
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]:
            Playing = False

        if keys_pressed[pygame.K_RIGHT]:
            if racket_x < (SCREEN_WIDTH - RACKET_WIDTH):
                racket_x += 10

        if keys_pressed[pygame.K_LEFT]:
            if racket_x > 0:
                racket_x -= 10

        if InGame:
            if ball_direction == UP_RIGHT:
                if ball_x >= (SCREEN_WIDTH - BALL_WIDTH):
                    ball_direction = UP_LEFT
                elif ball_y <= 0:
                    ball_direction = DOWN_RIGHT
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
            elif ball_direction == DOWN_RIGHT:
                if ball_x >= (SCREEN_WIDTH - BALL_WIDTH):
                    ball_direction = DOWN_LEFT
                elif ball_y >= (SCREEN_HEIGHT - BALL_HEIGHT):
                    ball_direction = UP_RIGHT
                    ball_x = BALL_INITIAL_X
                    ball_y = BALL_INITIAL_Y
                    lifes -= 1
                    ball_speed = BALL_SPEED
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
            elif ball_direction == DOWN_LEFT:
                if ball_x <= 0:
                    ball_direction = DOWN_RIGHT
                elif ball_y >= (SCREEN_HEIGHT - BALL_HEIGHT):
                    ball_direction = UP_RIGHT
                    ball_x = BALL_INITIAL_X
                    ball_y = BALL_INITIAL_Y
                    lifes -= 1
                    ball_speed = BALL_SPEED
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
            elif ball_direction == UP_LEFT:
                if ball_x <= 0:
                    ball_direction = UP_RIGHT
                elif ball_y <= 0:
                    ball_direction = DOWN_LEFT
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed

        else:
            if keys_pressed[pygame.K_RETURN]:
                lifes = 3
                InGame = True

        screen.blit(background, (0, 0))
        screen.blit(racket, (racket_x, racket_y))
        screen.blit(ball, (ball_x, ball_y))

        if lifes > 0:
            initial_x = SCREEN_WIDTH - 30

            for _ in range(lifes):
                screen.blit(life, (initial_x, 0))
                initial_x -= 40
        else:
            InGame = False
            screen.blit(gameover, (200, 60))

        pygame.display.flip()

if __name__ == '__main__':
    main()

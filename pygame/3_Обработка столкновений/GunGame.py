import random
import sys

import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class ScoreBoard:
    def __init__(self):
        self.shots = 0
        self.hits = 0
        self.performance = 0
        self.font = pygame.font.SysFont('calibri', 20)
        self.text_shots = self.font.render(str(f'Shots: {self.shots}'), True, THECOLORS['white'])
        self.text_hits = self.font.render(str(f'Hits: {self.hits}'), True, THECOLORS['white'])
        self.text_performance = self.font.render(str(f'Performance: {self.performance}%'), True, THECOLORS['white'])

    def draw(self):
        screen.blit(self.text_shots, (50, 50))
        screen.blit(self.text_hits, (50, 80))
        screen.blit(self.text_performance, (50, 110))

    def when_shot(self):
        self.shots = self.shots + 1
        self.text_shots = self.font.render(str(f'Shots: {self.shots}'), True, THECOLORS['white'])
        self.performance = round(self.hits / self.shots * 100)
        self.text_performance = self.font.render(str(f'Performance: {self.performance}%'), True, THECOLORS['white'])

    def when_hit(self):
        self.hits = self.hits + 1
        self.text_hits = self.font.render(str(f'Hits: {self.hits}'), True, THECOLORS['white'])
        self.performance = round(self.hits / self.shots * 100)
        self.text_performance = self.font.render(str(f'Performance: {self.performance}%'), True, THECOLORS['white'])


class Cannon:
    def __init__(self):
        self.color = (172, 127, 127)
        self.cannon_shape = [(295, 460), (320, 410), (345, 460)]

    def draw(self):
        pygame.draw.polygon(screen, self.color, self.cannon_shape, 0)


class Bullet:
    def __init__(self):
        self.center = [320, 405]
        self.radius = 5
        self.color = (255, 0, 0)
        self.speed = 10
        self.shot_status = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.radius, 0)

    def move(self):
        self.center[1] = self.center[1] - self.speed
        if self.center[1] < 0:
            self.shot_status = 0
            self.center[1] = 405

    def when_collide(self):
        self.shot_status = 0
        self.center[1] = 405


class Target:
    def __init__(self):
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed = 5
        self.target = pygame.Rect(295, 0, 50, 20)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.target, 0)

    def move(self):
        if self.target[0] <= 0 or self.target[0] >= 590:
            self.speed = self.speed * - 1
        self.target[0] = self.target[0] + self.speed

    def when_collide(self):
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed = random.randint(5, 20) * self.speed / abs(self.speed)


def collide(target_shape, bullet_center):
    result = target_shape.collidepoint(bullet_center)
    return result


score_board = ScoreBoard()
cannon = Cannon()
bullet = Bullet()
target = Target()

while True:
    screen.fill(THECOLORS['black'])
    cannon.draw()

    bullet.draw()
    if bullet.shot_status == 1:
        bullet.move()

    target.draw()
    target.move()

    if collide(target.target, bullet.center) is True:
        target.when_collide()
        bullet.when_collide()
        score_board.when_hit()

    score_board.draw()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.shot_status = 1
                score_board.when_shot()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    pygame.time.delay(50)

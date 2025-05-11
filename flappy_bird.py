import pygame
import random

WIN_WIDTH = 500
WIN_HEIGHT = 700
PIPE_GAP = 200
GRAVITY = 1.5

class Bird:
    def __init__(self):
        self.y = 350
        self.x = 100
        self.vel = 0
        self.tick = 0
        self.jump()

    def jump(self):
        self.vel = -10
        self.tick = 0

    def move(self):
        self.tick += 1
        displacement = self.vel + GRAVITY * self.tick
        self.y += displacement
        return displacement

    def get_mask(self):
        return pygame.Rect(self.x, self.y, 30, 30)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 450)
        self.top = self.height - PIPE_GAP
        self.bottom = self.height + PIPE_GAP
        self.passed = False

    def move(self):
        self.x -= 5

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_rect = pygame.Rect(self.x, 0, 80, self.top)
        bottom_rect = pygame.Rect(self.x, self.bottom, 80, WIN_HEIGHT)
        return bird_mask.colliderect(top_rect) or bird_mask.colliderect(bottom_rect)

class Base:
    def __init__(self):
        self.y = 630
        self.x1 = 0
        self.x2 = WIN_WIDTH

    def move(self):
        self.x1 -= 5
        self.x2 -= 5
        if self.x1 + WIN_WIDTH < 0:
            self.x1 = self.x2 + WIN_WIDTH
        if self.x2 + WIN_WIDTH < 0:
            self.x2 = self.x1 + WIN_WIDTH

class FlappyGame:
    def __init__(self):
        self.bird = Bird()
        self.pipes = [Pipe(600)]
        self.base = Base()
        self.score = 0
        self.frame = 0

    def step(self, flap):
        if flap:
            self.bird.jump()

        displacement = self.bird.move()
        add_pipe = False
        rem = []

        for pipe in self.pipes:
            pipe.move()
            if pipe.collide(self.bird):
                return self.get_state(), -1000, True
            if pipe.x + 80 < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < self.bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe(600))

        for r in rem:
            self.pipes.remove(r)

        if self.bird.y >= WIN_HEIGHT or self.bird.y < 0:
            return self.get_state(), -1000, True

        self.base.move()
        self.frame += 1
        return self.get_state(), 1, False

    def get_state(self):
        pipe = None
        for p in self.pipes:
            if p.x + 80 > self.bird.x:
                pipe = p
                break
        return [
            self.bird.y / WIN_HEIGHT,
            (pipe.height) / WIN_HEIGHT,
            (pipe.bottom) / WIN_HEIGHT,
            (pipe.x - self.bird.x) / WIN_WIDTH,
            self.bird.vel / 10
        ]

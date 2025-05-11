import os
import sys
import pickle
import pygame
from flappy_bird import FlappyGame
import neat

MODEL_PATH = "models/best_genome.pkl"
CONFIG_PATH = "config.txt"

# Check for trained model
if not os.path.isfile(MODEL_PATH):
    print(f"No trained model found at '{MODEL_PATH}'.")
    print("Please run:\n    python train.py\nfirst, to generate the model.")
    sys.exit(1)

# Load genome
with open(MODEL_PATH, "rb") as f:
    genome = pickle.load(f)

# Load NEAT config
config = neat.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    CONFIG_PATH
)

net = neat.nn.FeedForwardNetwork.create(genome, config)

# Initialize game & display
pygame.init()
win = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
game = FlappyGame()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    state = game.get_state()
    output = net.activate(state)
    _, _, done = game.step(output[0] > 0.5)

    # Draw
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 0), pygame.Rect(game.bird.x, game.bird.y, 30, 30))
    for pipe in game.pipes:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pipe.x, 0, 80, pipe.top))
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pipe.x, pipe.bottom, 80, 700))
    pygame.draw.rect(win, (150, 75, 0), pygame.Rect(0, game.base.y, 500, 70))
    pygame.display.update()

    clock.tick(30)

pygame.quit()
import os
import sys
import pickle
import pygame
from flappy_bird import FlappyGame
import neat

MODEL_PATH = "models/best_genome.pkl"
CONFIG_PATH = "config.txt"

# Check for trained model
if not os.path.isfile(MODEL_PATH):
    print(f"No trained model found at '{MODEL_PATH}'.")
    print("Please run:\n    python train.py\nfirst, to generate the model.")
    sys.exit(1)

# Load genome
with open(MODEL_PATH, "rb") as f:
    genome = pickle.load(f)

# Load NEAT config
config = neat.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    CONFIG_PATH
)

net = neat.nn.FeedForwardNetwork.create(genome, config)

# Initialize game & display
pygame.init()
win = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
game = FlappyGame()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    state = game.get_state()
    output = net.activate(state)
    _, _, done = game.step(output[0] > 0.5)

    # Draw
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 0), pygame.Rect(game.bird.x, game.bird.y, 30, 30))
    for pipe in game.pipes:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pipe.x, 0, 80, pipe.top))
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pipe.x, pipe.bottom, 80, 700))
    pygame.draw.rect(win, (150, 75, 0), pygame.Rect(0, game.base.y, 500, 70))
    pygame.display.update()

    clock.tick(30)

pygame.quit()

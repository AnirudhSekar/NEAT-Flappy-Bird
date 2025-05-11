import neat
import pickle
from flappy_bird import FlappyGame

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        game = FlappyGame()
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = 0
        done = False

        while not done:
            state = game.get_state()
            output = net.activate(state)
            flap = output[0] > 0.5
            _, reward, done = game.step(flap)
            genome.fitness += reward

if __name__ == "__main__":
    config_path = "config.txt"
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    pop.add_reporter(neat.StatisticsReporter())
    pop.add_reporter(neat.Checkpointer(10))

    winner = pop.run(eval_genomes, 50)

    with open("models/best_genome.pkl", "wb") as f:
        pickle.dump(winner, f)

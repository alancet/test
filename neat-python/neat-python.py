
# coding: utf-8

# In[6]:


"""2-input xor example.
"""
import os
import neat
import visualize

xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_outputs = [(0.0,), (1.0,), (1.0,), (0.0,)]

print('xor_inputs', xor_inputs)
print('xor_outputs', xor_outputs)


# In[15]:


print(os.getcwd)


# In[22]:


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2


local_dir = os.getcwd()
config_file = os.path.join(local_dir, 'config-feedforward')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    config_file)
p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(neat.Checkpointer(5))

winner = p.run(eval_genomes, 300)

print('----------------------------------------------------------------------------------------------------------')
print('\nBest genome:\n{!s}'.format(winner))

print('\nOutput:')


# In[25]:


winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

for xi, xo in zip(xor_inputs, xor_outputs):
    output = winner_net.activate(xi)
    print('input {!r}, expected output {!r}, got {!r}'.format(xi, xo, output))


# In[27]:


node_names = {-1: 'A', -2: 'B', 0: 'A XOR B'}
visualize.draw_net(config, winner, True, node_names=node_names)


# In[30]:


visualize.plot_stats(stats, ylog=False, view=True)


# In[32]:


visualize.plot_species(stats, view=True)


# In[33]:


p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
p.run(eval_genomes, 10)


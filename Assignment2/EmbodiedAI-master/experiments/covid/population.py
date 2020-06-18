import numpy as np
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p

class Population(Swarm):

    def __init__(self, screen_size):
        super(Population, self).__init__(screen_size)
        self.object_loc = p.OUTSIDE

    def initialize(self, num_agents, swarm):

        # add obstacle/-s to the environment if present
        if p.OBSTACLES:
            object_loc = p.OBJECT_LOC

            if p.OUTSIDE:
                scale = [300, 300]
            else:
                scale = [800, 800]

            filename = 'experiments/flocking/images/convex.png' if p.CONVEX else 'experiments/flocking/images/redd.png'

            self.objects.add_object(file=filename, pos=object_loc, scale=scale, type='obstacle')

            min_x, max_x = helperfunctions.area(object_loc[0], scale[0])
            min_y, max_y = helperfunctions.area(object_loc[1], scale[1])

        # add agents to the environment
        for agent in range(num_agents):
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # if obstacles present re-estimate the coordinates
            if p.OBSTACLES:
                if p.OUTSIDE:
                    while coordinates[0] <= max_x and coordinates[0] >= min_x and coordinates[1] <= max_y and \
                            coordinates[1] >= min_y:
                        coordinates = helperfunctions.generate_coordinates(self.screen)
                else:
                    while coordinates[0] >= max_x or coordinates[0] <= min_x or coordinates[1] >= max_y or coordinates[
                        1] <= min_y:
                        coordinates = helperfunctions.generate_coordinates(self.screen)

            self.add_agent(Person(pos=np.array(coordinates), v=None, population=swarm))


    def find_neighbor_separation(self, person, neighbors):  # show what works better
        separate = np.zeros(2)
        for idx in neighbors:
            neighbor_pos = list(self.agents)[idx].pos
            difference = person.pos - neighbor_pos  # compute the distance vector (v_x, v_y)
            difference /= helperfunctions.norm(
                difference)  # normalize to unit vector with respect to its maginiture
            separate += difference  # add the influences of all neighbors up
        return separate / len(neighbors)
import pygame
import numpy as np
from simulation.agent import Agent
from simulation import helperfunctions
from experiments.covid import parameters as p


"""
Specific Person properties and helperfunctions 
"""

class Person(Agent):
    def __init__(self, pos, v, population, image='experiments/covid/images/orange.png'):
        super(Person,self).__init__(pos,v,image,
                                  max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                  mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                  dT=p.dT)

        self.population = population


    def update_actions(self):

        #avoid any obstacles in the environment
        for obstacle in self.population.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()


    def neighbor_action(self):
        sick_prob =np.zeros(2)
        neighbors = self.population.find_neighbors(self, p.RADIUS_VIEW)

        #if neighbors:


    def susceptibility(self, neighbour_center):
        """
        Function to return a probability that determines whether a person gets sick
        or not
        """
        probability = neighbour_center - self.pos
        return probability






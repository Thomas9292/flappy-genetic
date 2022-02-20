import random

from .base import BaseAgent


class RandomAgent(BaseAgent):
    def predict_jump(self, horizontal_dist, vertical_dist):
        return random.randint(1, 18) == 1

    def mutate(self):
        pass

    def breed(predictorA, predictorB):
        pass

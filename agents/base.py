from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    def predict_jump(self, horizontal_dist, vertical_dist):
        pass

    @abstractmethod
    def mutate(self):
        pass

    @staticmethod
    @abstractmethod
    def breed(predictorA, predictorB):
        pass

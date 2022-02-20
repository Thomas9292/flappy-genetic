from flappy_game import FlappyGame
from agents.random import RandomAgent

game = FlappyGame()
agents = [RandomAgent(), RandomAgent(), RandomAgent(), RandomAgent(), RandomAgent(), RandomAgent()]


for i in range(10):
    crashInfo = game.mainGame(game.movementInfo, agents)
    print(crashInfo["fitness"])
    game.showGameOverScreen(crashInfo)

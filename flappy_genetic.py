from flappy_game import FlappyGame
from agents.random import RandomAgent

game = FlappyGame()
agent = RandomAgent()


for i in range(10):
    crashInfo = game.mainGame(game.movementInfo, agent)
    print(crashInfo)
    game.showGameOverScreen(crashInfo)

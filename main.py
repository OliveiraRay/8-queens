from utils.environment import *
from utils.agent import *

def run():
    env = Espaco(shape_x=8, shape_y=8)
    agent = Agente(espaco=env)
    agent.load_results()

if __name__ == "__main__":
    run()
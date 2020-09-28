from pico2d import *
import random

RES_DIR = '../res'

def rand(val):
    return val * random.uniform(0.9, 1.1)

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        
    def draw(self):
        self.image.draw(400, 30)
        
    def update(self):
        pass

if __name__=='__main__':
    print("Running test code ^_^")

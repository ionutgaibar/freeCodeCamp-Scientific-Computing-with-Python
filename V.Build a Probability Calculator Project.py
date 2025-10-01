import copy
import random

class Hat:

    def __init__(self, **kwargs):
        if len(kwargs):
            self.contents = []
            for i,j in kwargs.items():
                for _ in range(j):
                    self.contents.append(i)
            self.HatContents  = self.contents.copy()

    def draw(self, number):
        drawn_items = []
        hat = self.contents
        if number >= len(hat):
            self.contents = []
            return hat
        for i in range(number):
            randomnr = random.randint(0, len(hat)-1)
            drawn_items.append(hat[randomnr])
            hat.pop(randomnr)
        return drawn_items

    def reset(self):
        self.contents = self.HatContents.copy()
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    CF = 0

    for _ in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                success = False
                break
        if success:
            CF += 1
        hat.reset()

    return CF / num_experiments

import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        # self.hat_balls = dict()
        for color, num in kwargs.items():
            # self.hat_balls[color] = num
            for i in range(num):
                self.contents.append(color)

    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else:
            random_balls = list()

            for i in range(n):
                single_draw = random.choice(self.contents)
                random_balls.append(single_draw)
                self.contents.pop(self.contents.index(single_draw))

            return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probab_counter = 0

    for experiment in range(num_experiments):
        exper_hat = copy.deepcopy(hat)
        sample_list = exper_hat.draw(num_balls_drawn)
        sample_dict = {color: sample_list.count(color) for color in set(sample_list)}
        match_condition = True

        for color, num in expected_balls.items():
            if color in sample_dict and expected_balls[color] <= sample_dict[color]:
                continue
            else:
                match_condition = False

        if match_condition:
            probab_counter += 1

    return probab_counter / num_experiments

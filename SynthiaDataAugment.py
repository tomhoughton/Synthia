from copyreg import constructor


class DataAugmentor:
    def __init__(self, data, consistency, dynamics, brightness, evolution) -> None:
        self.df = data
        self.stats_consistency = consistency
        self.stats_brightness = brightness
        self.stats_dynamics = dynamics
        self.stats_evolution = evolution

    def display_dataset(self):
        print('The Dataset')
        print(self.df)

    

    
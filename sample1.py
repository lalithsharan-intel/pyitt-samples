import pyitt
import random

class SampleWorkload:
    def __init__(self):
        pass
    @pyitt.task
    def RandomNumbers(self):
        print('RandomNumbers')
        random_numbers = [random.randint(1, 10) for _ in range(10000)]
        squared_numbers = [x**2 for x in random_numbers]
        print (sum(squared_numbers))
    @pyitt.task
    def Run(self):
        print('Run')
        self.RandomNumbers()
if __name__ == "__main__":
    wl = SampleWorkload()
    wl.Run()

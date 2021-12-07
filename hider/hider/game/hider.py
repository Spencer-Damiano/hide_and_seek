import random

class Hider:

    def __init__(self):
        self._location = random.randint(1, 1000)
        self._distance = [1001]


    def watch(self, seeker):
        self._distance.append(self._location - seeker.get_location())


    def get_hint(self):
        
        distance_1 = self._distance[-1]
        distance_2 = self._distance[-2]

        if distance_1 < 0: distance_1 *= -1
        if distance_2 < 0: distance_2 *= -1

        if distance_1 == 0:
            return "you found me!"
        elif distance_1 < distance_2:
            return "warmer"
        elif distance_1 > distance_2:
            return "colder"

    
    def is_found(self):
        if self._distance[-1] == 0:
            return True

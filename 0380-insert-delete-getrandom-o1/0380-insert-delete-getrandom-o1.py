from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.randomized_set = {}

    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        self.randomized_set[val] = True
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            del self.randomized_set[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
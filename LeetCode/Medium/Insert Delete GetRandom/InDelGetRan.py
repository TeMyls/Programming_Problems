import random
class RandomizedSet:

    def __init__(self):
        self.st = set()
        return None
        

    def insert(self, val: int) -> bool:
        if val not in self.st:
            self.st.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.st:
            self.st.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        if len(self.st) == 1:
            return list(self.st)[0]
        else:
            return random.choice(list(self.st))

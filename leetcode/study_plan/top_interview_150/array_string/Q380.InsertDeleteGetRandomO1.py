class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        self.n = -1

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        # Map with list position
        self.dict[val] = len(self.list)
        self.list.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        #Swap with last list position
        self.dict[self.list[-1]] = self.dict[val]
        self.list[self.dict[val]], self.list[-1] = self.list[-1], self.list[self.dict[val]]
        self.list.pop()
        del self.dict[val]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, self.n)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

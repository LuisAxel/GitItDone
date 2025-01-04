class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.s = set()
        self.heap = []

    def popSmallest(self) -> int:
        if not self.heap:
            self.smallest += 1
            return self.smallest - 1

        res = heappop(self.heap)
        self.s.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if self.smallest > num and num not in self.s:
            self.s.add(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        self.len_small = 0
        self.len_large = 0

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if self.len_large + 1 > self.len_small:
            heappush(self.small, -heappop(self.large))
            self.len_small += 1
        else:
            self.len_large += 1

    def findMedian(self) -> float:
        # total % 2 == 0
        if self.len_small == self.len_large:
            return (self.large[0] - self.small[0]) / 2
        return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class RecentCounter:

    def __init__(self):
        self.req = []
        self.range = deque()

    def ping(self, t: int) -> int:
        self.req.append(t)
        self.range.append(t)

        while self.range and self.range[0] < t - 3000:
            self.range.popleft()

        return len(self.range)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

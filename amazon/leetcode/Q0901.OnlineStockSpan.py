class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
        else:
            counter = 1
            while self.stack and self.stack[-1][0] <= price:
                counter += self.stack[-1][1]
                self.stack.pop()
            self.stack.append((price, counter))
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

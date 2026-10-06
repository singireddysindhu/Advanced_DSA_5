#901
class StockSpanner:
    def __init__(self):   
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        self.stack.append((price, span))

        return span
a=["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
b=[[], [100], [80], [60], [70], [60], [75], [85]]
print(a[0], b[0])
obj = StockSpanner()

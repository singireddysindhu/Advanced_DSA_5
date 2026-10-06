def next_Greater(arr):
    n=len(arr)
    result=[-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<arr[i]:
            index=stack.pop()
            result[index]=arr[i]
        stack.append(i)
    return result
arr=[2,1,5,3,4]
print(next_Greater())


'''
#901. Online Stock Span
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''

'''
#496. Next Greater Element I
class Solution:

    def nextGreaterElement(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]
'''

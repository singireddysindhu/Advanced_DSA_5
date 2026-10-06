#leetcode 496
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    d = {}
    for i in range(len(nums2)-1,-1,-1):
        cur=nums2[i]
        while stack and stack[-1] < cur:
            stack.pop()
        if stack:
            d[cur] = stack[-1]
        else:
            d[cur] = -1
        stack.append(cur)
    res = []
    for ele in nums1:
        res.append(d[ele])
    return res
nums1 = [0,5,6]
nums2 = [1,0,2,5,6]
print(next_greater_element(nums1, nums2))




#239. Sliding Window Maximum 
def maxSlidingWindow(nums, k):
    window = nums[:k]
    res = [max(window)]
    for i in range(0, len(nums) - k+1):
        
        res.append(max(window))
    return res
  
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))

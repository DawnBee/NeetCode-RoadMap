"""
*=Sliding Window Maximum=*
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import deque

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    res = []
    queue = deque()
    left = right = 0

    while right < len(nums):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)

        # Remove left val from window
        if left > queue[0]:
            queue.popleft()
        
        if (right - left + 1) >= k:
            res.append(nums[queue[0]])
            left += 1
        right += 1
    
    return res


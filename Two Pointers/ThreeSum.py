"""
*=Three Sum=*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for index, val in enumerate(nums):
        if index > 0 and val == nums[index - 1]:
            continue
            
        left, right = index + 1, len(nums) - 1

        # Two Pointer O(n) - Time
        while left < right:
            three_sum = val + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append([val, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res
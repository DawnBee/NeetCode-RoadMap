"""
*=Longest Consecutive Sequence=*
Given an array of integers nums, return the length 
of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in 
which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].
"""
from typing import List

def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in nums:
        # Checks if start of seq
        if num - 1 not in num_set:
            length = 0
            
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    
    return longest
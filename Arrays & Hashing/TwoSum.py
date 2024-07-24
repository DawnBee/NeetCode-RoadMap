"""
*=Two Sum=*

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target. You may assume that
each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

from typing import List

# Method #1: Two Pointers
def m1_two_sum(nums: List[int], target: int) -> List[int]:
    # O(n) - Time
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Method #2: Prefix Diff
def m2_two_sum(nums: List[int], target: int) -> List[int]:
    prev_map = {} # O(1) - Space

    for i, n in enumerate(nums): # O(n) - Time
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
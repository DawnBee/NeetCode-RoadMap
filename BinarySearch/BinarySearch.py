"""
*=Binary Search=*
You are given an array of distinct integers nums, sorted in ascending order, 
and an integer target. Implement a function to search for target within nums. 
If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3
"""
from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
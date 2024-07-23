"""
    *=Contains Duplicate=*
    Given an integer array nums, return true if any value appears 
    at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false
"""

from typing import List

# Method #1: Using a set()
def m1_contains_duplicate(nums: List[int]) -> bool:
    seen = set() # O(1) - Space

    # O(n) - Time
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Method #2: Using sort()
def m2_contains_duplicate(nums: List[int]) -> bool:
    # O(n log n) - Time
    nums.sort()

    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


# Method #3: Using built-in Counter() dictionary
def m3_contains_duplicate(nums: List[int]) -> bool:
    from collections import Counter
    num_counts = Counter(nums) # O(1) - Space

    for val in num_counts.values():
        if val > 1:
            return True
    return False
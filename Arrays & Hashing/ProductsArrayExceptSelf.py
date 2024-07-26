"""
*=Product of Array Except Self=*
Given an integer array nums, return an array output where output[i] is 
the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time 
without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
"""
from typing import List

# Method #1: Using 2 lists
def m1_product_except_self(nums : List[int]) -> List[int]:
    N = len(nums)

    # O(2n) - Time
    # O(2n) - Space
    left = [1] * N
    for i in range(1, N):
        left[i] = left[i - 1] * nums[i - 1]
    
    right = [1] * N
    for i in range(N-2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    ans = [1] * N
    for i in range(N):
        ans[i] = left[i] * right[i]
    
    return ans


# Method #2: Using 'pre' & 'post' variables
def m2_product_except_self(nums : List[int]) -> List[int]:
    result = [1] * len(nums) # O(n) - Space
    pre, post = 1, 1

    # O(2n) - Time
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]

    for i in range(len(nums)-1,-1,-1):
        result[i] *= post 
        post *= nums[i]
    return result
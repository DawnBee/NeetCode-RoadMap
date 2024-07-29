"""
*=Max Water Container=*
You are given an integer array heights where heights[i] represents 
the height of the ith bar. You may choose any two bars to form a container. 
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
"""
from typing import List

def max_area(heights: List[int]) -> int:
    left, right = 0, len(heights)-1
    max_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
            
    return max_area
"""
*=Trapping Rain Water=*
You are given an array non-negative integers heights which represent an elevation map. 
Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
"""
from typing import List

# Method #1: Two Pointers
def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    res = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]
    return res


# Method #2: Having left and right sublists based on the highest wall
def trap(height: List[int]) -> int:
    highest_level = height.index(max(height))

    volume = 0
    # Contains blocks from the left and right of the highest block
    for level in [height[:highest_level], height[:highest_level:-1]]:
        first = 0
        for block in level:
            if block < first:
                volume += first - block
            else:
                first = block
    return volume
"""
*=Largest Rectangle in Histogram=*

You are given an array of integers heights where heights[i] represents the height of a bar. 
The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8
"""
from typing import List

def largest_rectangle_area(heights : List[int]) -> int:
    max_area = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i -index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area
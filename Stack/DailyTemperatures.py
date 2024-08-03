"""
*=Daily Temperatures=*
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""

from typing import List

# Method #1: Using 'monotonically decreasing stack'
def m1_daily_temperatures(temperatures : List[int]) -> List[int]:
    res = [0] * len(temperatures) # O(n) - Space
    stack = []

    for index, temp in enumerate(temperatures): #O(n) - Time
        while stack and temp > stack[-1][0]:
            stack_temp, stack_index = stack.pop()
            res[stack_index] = index - stack_index
        stack.append([temp, index])
    
    return res


# Method #2: Brute Force O(n^2)
def m2_daily_temperatures(temperatures : List[int]) -> List[int]:
    res = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        count = 0
        for j in range(i + 1, len(temperatures)):
            count += 1
            
            if temperatures[j] > temperatures[i]:
                res[i] = count
                break
    
    return res
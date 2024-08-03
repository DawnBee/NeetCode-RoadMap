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
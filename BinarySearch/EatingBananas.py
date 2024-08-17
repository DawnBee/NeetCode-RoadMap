"""
*=Koko Eating Bananas=*
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
"""
import math
from typing import List

def min_eating_speed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    result = right

    while left <= right:
        speed = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)

        if hours <= h:
            result = min(result, speed)
            right = speed - 1
        else:
            left = speed + 1
    return result
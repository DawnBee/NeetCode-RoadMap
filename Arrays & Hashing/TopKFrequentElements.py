"""
*=Top K Frequent Elements=*
Given an integer array nums and an integer k, 
return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
from typing import List

# Method #1: Using Counter()
def m1_top_k_freq_elem(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    num_counts = Counter(nums) # O(1) - Space
    top_k = num_counts.most_common(k)
    
    result = [n for n, _ in top_k] # O(n) - Time
    return result


# Method #2: Bucket sorting
def m2_top_k_freq_elem(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums)+1)] # O(n + 1) - Space
    # Indices corresponds to frequency

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for key, value in count.items():
        freq[value].append(key)
    
    result = []

    for i in range(len(freq)-1, 0, -1): # O(n + m) - Time
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
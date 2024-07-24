"""
*=Group Anagrams=*

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the 
original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List
from collections import defaultdict

# Method #1: Pre-built dictionary with 'n' times alphabets' total
def group_anagrams(words: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for s in words:  # O(n * k) - Time
        count = [0] * 26 # O(26) - Space
        for c in s:
            count[ord(c) - ord('a')] += 1
        result[tuple(count)].append(s)
    return result.values()


# Method #2: Using sorts
def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list) # O(1) - Space

    for word in words:
        sorted_word = ''.join(sorted(word)) # O(n log n) - Time
        anagrams[sorted_word].append(word)

    return list(anagrams.values())
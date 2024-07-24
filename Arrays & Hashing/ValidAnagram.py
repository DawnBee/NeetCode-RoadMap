"""
*=Valid Anagram=*

Given two strings s and t, return true if t is an anagram of s, 
and false otherwise. An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# Method #1: Using sort()
def m1_is_anagram(s: str, t: str) -> bool:
    # Naive Approach
    s_list, t_list = [l.lower() for l in s], [l.lower() for l in t]
    s_list.sort(), t_list.sort() # O(n log n) - Time
    
    return t_list == s_list


# Method #2: Using dictionary
def m2_is_anagram(s: str, t: str) -> bool:
    s_counts, t_counts = {}, {} # O(1) * 2 = O(1) -Space

    for char in s:
        s_counts[char] = s_counts.get(char, 0) + 1

    for char in t:
        t_counts[char] = t_counts.get(char, 0) + 1
    
    return s_counts == t_counts


# Method #3: Using built-in Counter() dictionary
def m3_is_anagram(s: str, t: str) -> bool:
    from collections import Counter
    s_counts, t_counts = Counter(s), Counter(t)

    return s_counts == t_counts
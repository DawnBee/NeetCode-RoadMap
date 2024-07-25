"""
*=String Encode and Decode=*
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
"""

from typing import List
class Solution:
    # Adds the length of the word and a non-alphabet
    # character in front of the word, thus: neet -> 4#neet
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # Ensures to decode the exact range of the word
    # by the help of the "len(s)#" placeholders
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
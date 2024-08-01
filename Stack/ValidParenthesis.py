"""
*=Valid Parentheses=*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

# The main idea to all these methods is to use 'stack' to
# track all the remaining 'open parenthesis' and check if we 
# encounter its 'closing' pair.

# Method #1
def m1_is_valid(s: str) -> bool:
    brackets = {')':'(', '}':'{', ']':'['}
    stack = []

    for c in s:
        # Checks if 'c' was a closing bracket
        if stack and c in brackets and brackets[c] == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    
    # If stack is empty means all the parenthesis has pairs
    # and we return 'true' otherwise false.
    return False if stack else True


# Method #2
def m2_is_valid(s: str) -> bool:
    stack = []
    close_open = {')':'(','}':'{',']':'['}

    for char in s:
        if char in close_open:
            if stack and stack[-1] == close_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


# Method #3
def m3_is_valid(s: str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack    
"""
*=Evaluate Reverse Polish Notation=*
You are given an array of strings tokens that represents a 
valid arithmetic expression in Reverse Polish Notation. Return the integer
that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

# Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
"""
from typing import List

def eval_RPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if stack and token == "+":
            stack.append(stack.pop() + stack.pop())
        elif stack and token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif stack and token == "*":
            stack.append(stack.pop() * stack.pop())
        elif stack and token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(token))
    
    return stack[0]
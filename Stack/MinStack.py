"""
*=Min Stack=*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

# Top solutions on LeetCode uses an aggregate function "min()"
# which I think defeats the purpose of the problem, the idea here
# is that they want us to create a "MinStack" using a 
# 'Monotonically Decreasing Stack'.

# Method #1: Not using 'min()'
class MinStack:
    def __init__(self):
        self.stack = [] # O(n) - Space
        self.min_stack = [] # O(n) - Space

    def push(self, val: int) -> None: # O(1) - Time
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None: # O(1) - Time
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        
    def top(self) -> int: # O(1) - Time
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int: # O(1) - Time
        if self.min_stack:
            return self.min_stack[-1]
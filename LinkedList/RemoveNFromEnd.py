"""
*=Remove Nth node from end of list=*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
# 1 --> 2 --> 3 --> 4 --> 5, n = 2
# 1 --> 2 --> 3 --> 5

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_llist(head):
    curr = head
    
    while curr:
        if not curr.next:
            print(curr.val)
        else:
            print(curr.val, end=" --> ")
        curr = curr.next

def remove_n_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = head, head

    for _ in range(n + 1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

    
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print_llist(node_1)
print_llist(remove_n_from_end(node_1, 3))
"""
*=Reverse LinkedList=*
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
> 1 -> 2 -> 3 -> 4 -> 5
> 5 -> 4-> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        if current.next is None:
            print(current.val)
        else:
            print(current.val, end=" --> ")
        current = current.next

# Recursive
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    
    if not head:
        return None

    new_head = head

    if head.next:
        new_head = reverse_list(head.next)
        head.next.next = head
    head.next = None

    return new_head

# Iterative
def reverse_list_2(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        val = curr.next
        curr.next = prev
        prev = curr
        curr = val
    
    return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
print_linked_list(head)
# print_linked_list((reverse_list(head)))
# print_linked_list((reverse_list_2(head)))
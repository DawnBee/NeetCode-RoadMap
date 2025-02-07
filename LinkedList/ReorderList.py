"""
*=Reorder List=*
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_llist(head):
    curr = head
    
    while curr:
        if curr.next is None:
            print(curr.val)
        else:
            print(curr.val, end=" --> ")
        curr = curr.next

def reorder(head: Optional[ListNode]) -> Optional[ListNode]:
    # Find mid
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse list
    second = slow.next
    prev = slow.next = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Merging
    first, second = head, prev

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    return head


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

# [1,2,3,4]
print_llist(reorder(node_1))
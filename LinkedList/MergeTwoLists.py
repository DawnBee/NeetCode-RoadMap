"""
*=Merge Two Sorted Linkedlist=*

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
from typing import Optional

# Definition for singly-linked list.
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

def merge_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
        list1 = list1.next
    elif list2:
        tail.next = list2
        list2 = list2.next

    return dummy.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(4)

node_1.next = node_2
node_2.next = node_3
llist_1 = node_1

node_a = ListNode(1)
node_b = ListNode(3)
node_c = ListNode(4)

node_a.next = node_b
node_b.next = node_c
llist_2 = node_a

print_linked_list(merge_lists(llist_1, llist_2))
# 1 --> 1 --> 2 --> 3 --> 4 --> 4
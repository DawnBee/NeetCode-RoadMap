"""
*=Linkedlist Cycle=*
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true

Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
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

def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def has_cycle_2(head):
    
    if not head:
        return False

    def search(slow, fast):
        
        if not fast or not fast.next:
            return False
        
        if slow == fast:
            return True
        
        return search(slow.next, fast.next.next)
    
    slow, fast = head, head.next

    return search(slow, fast)

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(4)
node_4 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2

print(has_cycle_2(node_1))
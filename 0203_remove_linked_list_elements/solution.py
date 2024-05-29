# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = None
        tail = None

        node = head
        while node:
            # cache the next node before references are mutated
            next = node.next

            if node.val != val:
                if not new_head:
                    new_head = node
                    new_head.next = None
                    tail = node
                else:
                    tail.next = node
                    tail = node
                    tail.next = None

            node = next

        return new_head
    
def printLL(head):
    values = []
    node = head
    while node:
        values.append(str(node.val))
        node = node.next
    print(",".join(values))

solution = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
four_1 = ListNode(4)
four_2 = ListNode(4)
five = ListNode(5)

four.next = one
one.next = five
five.next = four_1
four_1.next = three
three.next = two
two.next = four_2

printLL(four)
printLL(solution.removeElements(four, 4))

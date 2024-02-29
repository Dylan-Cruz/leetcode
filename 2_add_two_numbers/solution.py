from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # use two pointers to iterate over the lists of numbers
        # add the numbers in each place + carry over
        # if the numbers exceed 10, store the carry over to be used in the next op

        result = ListNode()
        result_pointer = result
        carry_over = 0

        while l1 or l2 or carry_over:
            # get the vals
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # do the math
            sum = l1_val + l2_val + carry_over
            digit = sum % 10
            carry_over = sum // 10

            # append the digit
            new_node = ListNode(digit)
            result_pointer.next = new_node
            result_pointer = new_node

            # update our pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


solution = Solution()

# 3285
num_1_thousands = ListNode(3)
num_1_hundreds = ListNode(2, num_1_thousands)
num_1_tens = ListNode(8, num_1_hundreds)
num_1_ones = ListNode(5, num_1_tens)

# 905
num_2_hundreds = ListNode(9)
num_2_tens = ListNode(0, num_2_hundreds)
num_2_ones = ListNode(5, num_2_tens)

answer_head = solution.addTwoNumbers(num_1_ones, num_2_ones)

while answer_head:
    print(answer_head.val)
    answer_head = answer_head.next

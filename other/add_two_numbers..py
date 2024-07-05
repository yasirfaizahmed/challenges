# flake8: noqa
from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        current_node: ListNode = l1
        while current_node is not None:
            l1_list.insert(0, current_node.val)
            current_node = current_node.next
        l2_list = []
        current_node: ListNode = l2
        while current_node is not None:
            l2_list.insert(0, current_node.val)
            current_node = current_node.next

        if len(l1_list) > len(l2_list):
            for _ in range(len(l1_list) - len(l2_list)):
                l2_list.insert(0, 0)
        elif len(l1_list) < len(l2_list):
            for _ in range(len(l2_list) - len(l1_list)):
                l1_list.insert(0,0)

        final_l = []
        carry = 0
        i = len(l1_list) - 1
        while i != -1:
            sum = l1_list[i] + l2_list[i] + carry
            if sum > 9:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
            print(sum)
            i -= 1
            final_l.append(sum)
            if i == -1 and carry == 1:
                final_l.append(carry)
            

        root_node = None
        prev_node = None
        for i in range(len(final_l)):
            if i == 0:
                root_node = ListNode(val=final_l[i])
                prev_node = root_node
            else:
                prev_node.next = ListNode(val=final_l[i])
                prev_node = prev_node.next

        return root_node


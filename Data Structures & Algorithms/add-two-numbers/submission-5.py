# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode()

        tmp1, tmp2, tmp3 = l1, l2, resHead

        while tmp1 or tmp2:

            val1 = tmp1.val if tmp1 else 0
            val2 = tmp2.val if tmp2 else 0

            if val1 + val2 + tmp3.val >= 10:
                tmp3.val = (val1 + val2 + tmp3.val) - 10
                tmp3.next = ListNode(val=1)
            else:
                tmp3.val = (val1 + val2 + tmp3.val)
                if tmp1 and tmp1.next or tmp2 and tmp2.next:
                    tmp3.next = ListNode()

            tmp1 = tmp1.next if tmp1 else None
            tmp2 = tmp2.next if tmp2 else None
            tmp3 = tmp3.next

        return resHead
        
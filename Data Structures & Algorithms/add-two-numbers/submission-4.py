# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #[5,6,7,1,2] and [5,5,4] [0,2,2,1]
        resHead = ListNode()

        tmp1, tmp2, tmp3 = l1, l2, resHead

        while tmp1 and tmp2:
            if tmp1.val + tmp2.val + tmp3.val >= 10:
                tmp3.val = (tmp1.val + tmp2.val + tmp3.val) - 10
                tmp3.next = ListNode(val=1)
            else:
                tmp3.val = (tmp1.val + tmp2.val + tmp3.val)
                if tmp1.next or tmp2.next:
                    tmp3.next = ListNode()

            tmp1 = tmp1.next
            tmp2 = tmp2.next
            tmp3 = tmp3.next

        if not tmp2:
            while tmp1:
                if tmp1.val + tmp3.val >= 10:
                    tmp3.val = (tmp1.val + tmp3.val) - 10
                    tmp3.next = ListNode(val=1)
                else:
                    tmp3.val = (tmp1.val + tmp3.val)
                    if tmp1.next:
                        tmp3.next = ListNode()

                tmp1 = tmp1.next
                tmp3 = tmp3.next
            
        elif not tmp1:
            while tmp2:
                if tmp3.val + tmp2.val >= 10:
                    tmp3.val = (tmp2.val + tmp3.val) - 10
                    tmp3.next = ListNode(val=1)
                else:
                    tmp3.val = (tmp2.val + tmp3.val)
                    if tmp2.next:
                        tmp3.next = ListNode()

                tmp2 = tmp2.next
                tmp3 = tmp3.next

        return resHead

        
            


        


        


        
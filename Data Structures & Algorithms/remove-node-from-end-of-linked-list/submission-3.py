# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        # Measure ListNode
        length = 0
        counter = head
        while counter:
            length+=1
            counter = counter.next

        # Find nth node from the end
        nth_frm_end = length - n
        deleter = dummy
        

        for node in range(nth_frm_end):
            deleter = deleter.next

        deleter.next = deleter.next.next


        return dummy.next

        


        '''
        [1,2,3,4,5,6,7,8,9]
        n = 2
        '''
        
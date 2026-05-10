# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Dividing ListNode
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        slow = head

        #Invert Fast List

        prev = None
        
        while fast:
            nxt = fast.next 
            fast.next = prev
            prev = fast 
            fast = nxt 

        #Merge Slow and Fast

        first = head
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

        
        
        



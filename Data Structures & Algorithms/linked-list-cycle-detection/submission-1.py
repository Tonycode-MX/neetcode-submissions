# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        pointer1 = head
        pointer2 = head

        while pointer2 and pointer2.next:
            if pointer2.next == pointer1 or pointer2.next.next == pointer1:
                return True
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
            
        return False

        
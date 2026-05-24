"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        tmp = head

        clones = {}

        while tmp:
            clones[tmp] = Node(tmp.val)
            tmp = tmp.next

        tmp = head

        while tmp:

            if tmp.next:
                clones[tmp].next = clones[tmp.next]

            if tmp.random:
                clones[tmp].random = clones[tmp.random]


            tmp = tmp.next

        return clones[head]

            



        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def remove(self, node):

        node.next = node.next.next

        return node
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #initialize dummy node

        node = ListNode(0, next = head)
        l,r = node, node
        i = 0
        while i <= n:
            r = r.next
            i += 1

        while r != None:
            l = l.next
            r = r.next

        self.remove(l)

        return node.next
        

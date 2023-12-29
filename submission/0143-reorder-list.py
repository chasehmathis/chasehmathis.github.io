# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head):
        if head == None:
            return None

        if head.next == None:
            return head

        node = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return node
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ## find middle of list

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow

        # reverse second half of ListNode

        last = self.reverse(middle)
        ret = head1 = head
        head2 = last

        while head1 and head2:

            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1
            
            head2.next = head1
            head2 = nxt2


        return ret
            

        

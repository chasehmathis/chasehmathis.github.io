# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ret = ListNode()
        curr = ret

        curr1 = list1; curr2 = list2

        while curr1 and curr2:
            if curr1.val > curr2.val:
                ret.next = ListNode(curr2.val)
                ret = ret.next
                curr2 = curr2.next
            else:
                ret.next = ListNode(curr1.val)
                ret = ret.next
                curr1 = curr1.next


        while curr1:
            ret.next = ListNode(curr1.val)
            ret = ret.next
            curr1 = curr1.next

        while curr2:
            ret.next = ListNode(curr2.val)
            ret = ret.next
            curr2 = curr2.next

        return curr.next

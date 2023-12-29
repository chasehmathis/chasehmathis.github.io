# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        ret = ListNode()
        curr = ret
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 and curr2:
            addition = curr1.val + curr2.val + carry
            if addition > 9:
                insert = addition - 10
                carry = 1
            else:
                insert = addition
                carry = 0

            curr.next = ListNode(insert)
            curr = curr.next
            print(insert)
            curr1 = curr1.next
            curr2 = curr2.next

            if not curr1 and not curr2 and carry:
                curr.next = ListNode(1)


        while curr1:
            addition = curr1.val + carry
            if addition > 9:
                insert = addition - 10
                carry = 1
            else:
                insert = addition
                carry = 0

            curr.next = ListNode(insert)
            curr = curr.next
            curr1 = curr1.next

            # if it ends with a carry
            if not curr1 and carry:
                curr.next = ListNode(1)

        while curr2:
            addition = curr2.val + carry
            if addition > 9:
                insert = addition - 10
                carry = 1
            else:
                insert = addition
                carry = 0

            curr.next = ListNode(insert)
            curr = curr.next
            curr2 = curr2.next
            if not curr2 and carry:
                curr.next = ListNode(1)

        return ret.next

            



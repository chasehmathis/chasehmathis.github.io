/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        
        if(head == null || head.next == null){
            return head;
        }
        ListNode ret = head.next;

        ListNode curr1 = head;
        ListNode curr2 = head.next;
        ListNode before = new ListNode();
        while(curr2 != null){
            ListNode temp = curr2.next;
            curr2.next = curr1;
            curr1.next = temp;
            before.next = curr2;
            before = curr1;
            curr1 = curr1.next;
            if(curr1 == null){
                break;
            }
            curr2 = curr1.next;
        
        }
        

        return ret;
    }
}

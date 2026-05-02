# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        n = 0
        while cur:
            n+=1
            cur = cur.next
        
        t = n//k
        pe = dummy

        while t:
            m = 0
            p1 = pe.next
            pee = pe
            pe = p1
            p2 = None
            while m<k:
                p3 = p1.next
                p1.next = p2
                p2 = p1
                p1 = p3
                m+=1
            pee.next = p2
            pe.next = p3
            t-=1
        return dummy.next
            
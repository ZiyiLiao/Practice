
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
     
        return a
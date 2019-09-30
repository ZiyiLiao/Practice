class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        
        
        while start and start.next:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
        
        return head
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dist = max(A) - min(A) - 2*K
        
        return dist if dist > 0 else 0
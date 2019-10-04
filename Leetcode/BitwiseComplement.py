class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 1
        i = 1
        while i <= N:
            i *= 2
            
        return i - N -1

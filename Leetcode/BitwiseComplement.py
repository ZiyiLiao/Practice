class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 1;
        i = 0
        while 2**i <= N:
            i += 1
            
        return 2**i - N -1

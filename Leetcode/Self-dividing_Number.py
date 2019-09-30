class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans =[]
        for i in range(left, right+1):
            if self.helper(i):
                ans.append(i)
        return ans
        
    def helper(self, tar):
        n = tar

        while n >= 10:
            digit = n%10
            if digit == 0:
                return False
            elif tar % digit != 0:
                return False
            else:
                n = int(n/10)
            
        if tar % n ==0:
            return True
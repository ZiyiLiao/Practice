class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        out = []
        while n not in out:
            out.append(n)
            n = self.helper(n)
               
           
        if out[-1] == 1:
            return True
        else:
            return False
        
    def helper(self,num):
        digit = (num % 10) **2
        while num >= 10:
            num = int(num/10)
            digit += (num % 10) **2
        return digit   
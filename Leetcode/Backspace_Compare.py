class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1 = self.helper(S)
        s2 = self.helper(T)
        
        return s1 == s2
        
        
    def helper(self,S):
        ans = []
        for i in range(len(S)):
            if S[i] != '#':
                ans.append(S[i])
            elif ans:
                ans.pop()
        return ans

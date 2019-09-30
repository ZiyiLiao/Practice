class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start = 0
        end = len(S)
        
        ans = []
        
        for i in range(len(S)):
            if S[i] == 'I':
                ans.append(start)
                start += 1
            else:
                ans.append(end)
                end -= 1
        
        ans.append(end)        
        return ans
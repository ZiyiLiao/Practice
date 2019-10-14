class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        left, right = 0, 0
        for char in S:
            if char == '(': 
                left += 1
                if left > 1:
                    res += char
            if char == ')':
                right += 1
                if right == left:
                    right, left = 0,0
                else:
                    res += char
                    
        return res
                

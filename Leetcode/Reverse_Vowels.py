class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end =len(s) - 1
        vowel = 'aeiouAEIOU'
        
        while start <= end:
            if s[start] not in vowel:
                start += 1
            elif s[end] not in vowel:
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                
        return ''.join(s)

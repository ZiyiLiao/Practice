class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        lst = S.split()
        vowel = "aeiouAEIOU"
        for i in range(len(lst)):
            if lst[i][0] not in vowel:
                lst[i] = lst[i][1:]  + lst[i][0] +"ma" + "a" *(i+1)
            else:
                lst[i] = lst[i] +"ma" + "a" *(i+1)
        
        return ' '.join(lst)



class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        dic = {}
        licensePlate = [x for x in licensePlate.lower() if x.isalpha()]
        n = len(licensePlate)
        
        for word in words:
            counts = []
            for char in licensePlate:
                if char in word:
                    counts.append(word.count(char)/licensePlate.count(char))
            if len(counts) == n:
                if (min(counts) >= 1) & (len(word) not in dic):
                    dic[len(word)] = word
                
        return dic[min(dic)]
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(word):
            return word.count(min(word))
        
        qs = [helper(q) for q in queries]
        ws = [helper(w) for w in words]
        
        
        ws = sorted(ws)
        ans = [0] * len(qs)
        
        for i,q in enumerate(qs):
            for j,w in enumerate(ws):
                if q < w:
                    ans[i] += len(ws) - j
                    break
        
        return ans

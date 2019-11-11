class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        
        count = 0
        while candies >= 0:
            ans[count%num_people] += count + 1 if count < candies else candies
            count += 1
            candies -= count
            
        return ans

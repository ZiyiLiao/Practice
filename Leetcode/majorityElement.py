class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = len(nums)/2
        cntr = collections.Counter(nums)
        for k, v in cntr.items():
            if v > cnt:
                return k

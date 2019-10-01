class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1)
        res = []
        
        for num in s:
            if num in nums2:
                res.append(num)
        return res

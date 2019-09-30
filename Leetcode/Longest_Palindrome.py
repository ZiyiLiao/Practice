class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        mini = len(list1) + len(list2)
        for i, a in enumerate(list1):
            for j, b in enumerate(list2):
                if a == b:
                    if mini >= i+j:
                        mini = i+j
                        res.append(a)
                        
        return res
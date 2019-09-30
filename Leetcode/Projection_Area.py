class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top , side = 0,0
        front = [0] * len(grid)
        
        for row in grid:
            top += (len(row) - row.count(0))
            side += max(row)
            for j in range(len(grid)):
                if row[j] > front[j]:
                    front[j] = row[j]
                    
                    
        return top + side + sum(front)
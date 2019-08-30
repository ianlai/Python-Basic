class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        if m is None or len(m)==0 or len(m[0])==0: 
            return False
        start = 0
        end = len(m) * len(m[0]) - 1

        if self.get(m, start) == target or self.get(m, end) == target:
            return True
        
        while start + 1 < end:
            mid = int((start + end) / 2)
            if self.get(m, mid) == target:
                return True
            if self.get(m, mid) > target: 
                end = mid
            if self.get(m, mid) < target: 
                start = mid
        return False
                
    def get(self, m, index):
        rowlen = len(m[0])
        row = index % rowlen 
        col = int(index / rowlen)
        return m[col][row]
        
            
class Solution:
    
    # Tabulation DP-2 [8%] 
    def numTrees(self, n: int) -> int:
        print("Tabulation DP-2")
        if n < 0:
            return -1
        if n <= 1: 
            return 1
 
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1): 
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]
        
    # =====================================================
    
    # Tabulation DP-1 [10%] 
    #
    # r(n): root is nth 
    # f0 = 1 (define)
    # f1 = 1 
    # f2 = 2
    # f3 = 5  = r(1)+r(2)+r(3)      = f0*f2 + f1*f1 + f2*f0         = 2 + 1 + 2     
    # f4 = 14 = r(1)+r(2)+r(3)+r(4) = f0*f3 + f1*f2 + f2*f1 + f3*f0 = 5 + 2 + 2 + 5 
    def numTrees1(self, n: int) -> int:
        print("Tabulation DP-1")
        if n < 0:
            return -1
        if n == 0: 
            return 1
        if n == 1:
            return 1
        arr = [0] * (n + 1)
        arr[0] = 1
        arr[1] = 1
        return self.dp(n, arr)
        
    def dp(self, n, arr):
        if arr[n] != 0:
            return arr[n]
        sum = 0
        for i in range(n):
            sum += self.dp(i, arr) * self.dp(n-i-1, arr) 
        arr[n] = sum
        return sum
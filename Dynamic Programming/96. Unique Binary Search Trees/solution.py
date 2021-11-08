"""
[1, 2] => 1 + 1 = 2
1 * 1      1 * 1
1          2
 \        /
  \      /
   2    1
   
[1, 2, 3] => 2 + 1 + 2 = 5
1 as root (left only one and right has two different)
2 as root (left and right only one)
3 as root (left two change and left only one)
1 * 2         1 * 1                    2 * 1     
1               2                        3
 \             / \                      /
  \           1   3                    2
   2                                  /
    \                                1
     \
      3

[1, 2, 3, 4] => 5 + 2 + 2 + 5 = 14
1 * 5 (3 nodes permutation)   ....
1
 \
  2
   \
    3
     \
      4



"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(n + 1):
            for j in range(i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        
        return dp[n]

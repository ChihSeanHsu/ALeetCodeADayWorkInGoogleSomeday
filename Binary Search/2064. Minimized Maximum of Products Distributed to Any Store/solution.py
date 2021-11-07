"""
We need to find out how many item we want to distribute to each store
It doesn't matter how many product in each type.

EX:
[1, 3, 5], n = 4
we distribute 1, 3 ,2 ,3
max = 3

We can search out 3 is the perfect number we want, 1, 2 or 3 does not matter because they all need for 1 store.

"""

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
      
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            # `(q + mid - 1) // mid` is to replace `ceil(q / mid)`
            if sum([(q + mid - 1) // mid for q in quantities]) > n:
                left = mid + 1
            else:
                right = mid
                
        return left

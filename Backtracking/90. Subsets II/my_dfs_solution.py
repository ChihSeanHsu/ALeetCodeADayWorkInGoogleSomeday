class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        def dfs(subset, candidates) -> List[List[int]]:
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue
                new_sub = subset.copy() + [candidates[i]]
                result.append(new_sub)
                dfs(new_sub, candidates[i + 1:len(candidates) + 1])

        dfs([], nums)
        return result
                

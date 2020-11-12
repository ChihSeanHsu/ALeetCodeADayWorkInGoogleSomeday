class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = {}
        nums = list(sorted(nums))
        self.get_permute(nums, result, visited, [], 0)  
        return result
    
    def get_permute(self, nums, result, visited, path, idx):
        if idx == len(nums):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if visited.get(i):
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited.get(i - 1):
                continue
            
            visited[i] = True
            path.append(nums[i])
            self.get_permute(nums, result, visited, path, idx + 1)
            path.pop()
            visited[i] = False

                
            

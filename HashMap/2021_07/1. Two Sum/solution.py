class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, i in enumerate(nums):
            item = mapping.get(i)
            if item is not None:
                return [item, idx]
            diff = target - i
            mapping[diff] = idx
                

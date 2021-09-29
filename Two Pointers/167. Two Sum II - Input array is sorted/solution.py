class Solution:
    # time: O(n) space: O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, i in enumerate(numbers, 1):
            if i in mapping:
                return [mapping[i][1], idx]
            
            mapping[target - i] = (i, idx)

    # time: O(n) space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            tmp = numbers[start] + numbers[end]
            if tmp == target:
                return [start + 1, end + 1]
            
            if tmp > target:
                end -= 1
            
            if tmp < target:
                start += 1

from collections import Counter

class Solution:
    # O(n) O(n)
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        count = 0
        for k, v in counter.items():
            if count < v:
                result = k
                count = v
        
        return result
    
    # O(nlogn) O(1)
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
        
    # O(n) O(1) Boyer-Moore Voting Algorithm
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

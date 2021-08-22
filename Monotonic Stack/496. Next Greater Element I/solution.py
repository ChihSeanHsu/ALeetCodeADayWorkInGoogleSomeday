# normal stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping_for_first = {}
        result = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                mapping_for_first[stack.pop()] = num
            stack.append(num)
            
        for num in nums1:
            result.append(mapping_for_first.get(num, -1))
        
        return result
 

# monotonic stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping_for_first = {}
        result = []

        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            mapping_for_first[num] = stack[-1] if stack else -1
            stack.append(num)

        for num in nums1:
            result.append(mapping_for_first.get(num, -1))

        return result

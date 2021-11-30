class Solution:
    # brute way O(n * n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        
        for c_idx in range(len(heights)):
            height = heights[c_idx]
            for p_idx in range(c_idx, -1, -1):
                height = min(height, heights[p_idx])
                result = max(result, height * (c_idx - p_idx + 1))
                
        return result
    
    # divide and conqure O(nlogn)
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculate(start, end):
            if start > end:
                return 0
            
            min_idx = start
            for idx in range(start, end + 1):
                if heights[idx] < heights[min_idx]:
                    min_idx = idx

            return max(
                heights[min_idx] * (end - start + 1),
                calculate(start, min_idx - 1),
                calculate(min_idx + 1, end),
            )
        return calculate(0, len(heights) - 1)

    # divide and conqure O(nlogn)
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        min_idx = 0
        
        for idx in range(len(heights)):
            if heights[idx] < heights[min_idx]:
                min_idx = idx
        
        return max(
            heights[min_idx] * len(heights),
            self.largestRectangleArea(heights[min_idx + 1:]),
            self.largestRectangleArea(heights[:min_idx]),
        )
    
    # stack O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        result = 0
        for idx in range(len(heights)):
            h = heights[idx]
            while stack[-1] != -1 and heights[stack[-1]] > h:
                prev_h = heights[stack.pop()]
                result = max(result, prev_h * (idx - stack[-1] - 1))
            stack.append(idx)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            result = max(result, h * (len(heights) - stack[-1] - 1))
        return result
        

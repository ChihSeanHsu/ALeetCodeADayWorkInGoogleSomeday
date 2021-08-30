class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        count = curr_sum = max_sum = start = 0
        end = minutes - 1
        curr_sum = sum([customers[i] for i in range(start, end + 1) if grumpy[i]])
        max_sum = curr_sum
        while start < len(customers):
            if grumpy[start]:
                curr_sum -= customers[start]
            else:
                count += customers[start]
            
            start += 1
            end += 1
            if end < len(customers) and grumpy[end]:
                curr_sum += customers[end]
                max_sum = max(curr_sum, max_sum)
        return count + max_sum

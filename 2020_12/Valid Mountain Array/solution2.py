class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = 0
        last_idx = len(arr) - 1
        if idx == last_idx:
            return False
        
        while idx < last_idx and arr[idx] < arr[idx + 1]:
            idx += 1

        if idx == last_idx or idx == 0:
            return False
        
        while idx < last_idx and arr[idx] > arr[idx + 1]:
            idx += 1
            
        return idx == last_idx

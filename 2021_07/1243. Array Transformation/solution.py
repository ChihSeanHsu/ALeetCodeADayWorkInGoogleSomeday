class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        tmp = []
        while tmp != arr:
            tmp = arr.copy()
            for i in range(1, len(arr) - 1):
                if tmp[i] < tmp[i - 1] and tmp[i] < tmp[i + 1]:
                    arr[i] += 1
                elif tmp[i] > tmp[i - 1] and tmp[i] > tmp[i + 1]:
                    arr[i] -= 1
                
        return arr

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        start, end = 0, reader.length() - 1  
        while start != end:
            _sum = (start + end)
            mid = _sum // 2
            ne = mid + 1
            if _sum % 2 == 0:
                mid = mid - 1
                
            res = reader.compareSub(start, mid, ne, end)
            if res == 1:
                end = mid
            elif res == -1:
                start = ne
            else:
                return mid + 1

        return start

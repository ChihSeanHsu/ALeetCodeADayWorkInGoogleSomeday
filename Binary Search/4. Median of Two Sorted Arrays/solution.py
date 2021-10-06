class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        a_start, a_end, b_start, b_end = 0, len(nums1) - 1, 0, len(nums2) - 1
        
        
        def search_kth( a_start, a_end, b_start, b_end, k):
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]


            mid_a, mid_b = (a_start + a_end) // 2, (b_start + b_end) // 2
            ele_a, ele_b = nums1[mid_a], nums2[mid_b]

            if k > mid_a + mid_b:
              # if ele_a > ele_b and k > 
                if ele_a > ele_b:
                    return search_kth(a_start, a_end, mid_b + 1, b_end, k)
                else:
                    return search_kth(mid_a + 1, a_end, b_start, b_end, k)
            else:
              # if ele_a > ele_b means right of a is bigger than all of b
                if ele_a > ele_b:
                    return search_kth(a_start, mid_a - 1, b_start, b_end, k)
                else:
                    return search_kth(a_start, a_end, b_start, mid_b - 1, k)
        
        if total % 2 != 0:
            return search_kth(a_start, a_end, b_start, b_end, total // 2)
        else:
            return (
                search_kth(a_start, a_end, b_start, b_end, total // 2) + 
                search_kth(a_start, a_end, b_start, b_end, total // 2 - 1)
            ) / 2
        
            
                
                

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        a = 0
        b = 0
        
        # [1, 2, 1, 3, 2, 5]
        for num in nums:
            xor ^= num
        
        # xor = 0 1 1 0
        mask = 1
        while (mask & xor == 0):
            mask = mask << 1
        
        # mask = 0 0 1 0  
        # make 3 and 5 split to two different variable
        # 3 = 0 1 1, 5 = 1 0 1, mask = 0 1 0 >>  3 xor with mask = 0 1 0, 5 xor with mask = 0 0 0
        for num in nums:
            if mask & num:
                a ^= num
            else:
                b ^= num
                
        return [a, b]

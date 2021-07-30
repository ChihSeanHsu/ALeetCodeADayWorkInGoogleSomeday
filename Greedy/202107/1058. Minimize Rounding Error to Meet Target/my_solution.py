from decimal import Decimal

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        float_arr = []
        for p in prices:
            int_part, float_part = p.split(".")
            target -= int(int_part)
            d = Decimal("." + float_part)
            if d:
                float_arr.append(d)
            
        if target > len(float_arr) or target < 0:
            return "-1"
    
        float_arr.sort()
        need_to_zero = len(float_arr) - target
        result = 0
        for i in range(need_to_zero):
            result += float_arr[i] - 0
        
        for i in range(need_to_zero, len(float_arr)):
            result += 1 - float_arr[i]
        

        return "{:.3f}".format(result)

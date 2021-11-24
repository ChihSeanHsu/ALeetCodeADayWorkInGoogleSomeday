class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        a_idx = 0
        b_idx = 0
        result = []
        
        while a_idx < len(firstList) and b_idx < len(secondList):
            a_l, a_r = firstList[a_idx]
            b_l, b_r = secondList[b_idx]
            new_l = max(b_l, a_l)
            new_r = min(b_r, a_r)
            if new_l <= new_r:
                result.append([new_l, new_r])
            
            if a_r < b_r:
                a_idx += 1
            else:
                b_idx += 1
                
        return result
        

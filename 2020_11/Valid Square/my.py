
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        length = set()
        array = [p1, p2, p3, p4]
        for idx, (x1, y1) in enumerate(array):
            for x2, y2 in array[idx+1:]:
                length.add(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2))
        length_list = list(length)
        if len(length_list) == 2:
            l1 = length_list[0]
            l2 = length_list[1]
            ninty_degree = round(l1 ** 2) * 2 == round(l2 ** 2) or round(l2 ** 2) * 2 == round(l1 ** 2)
            if ninty_degree:
                return True
        return False
            

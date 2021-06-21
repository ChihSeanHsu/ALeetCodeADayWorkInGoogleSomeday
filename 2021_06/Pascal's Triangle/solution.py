class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i + 1):
                if j == i:
                    tmp.append(1)
                else:
                    tmp.append(result[i-1][j - 1] + result[i-1][j])
            result.append(tmp)
        return result
                

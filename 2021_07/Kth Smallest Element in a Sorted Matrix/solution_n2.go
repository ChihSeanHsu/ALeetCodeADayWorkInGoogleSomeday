import "sort"

func kthSmallest(matrix [][]int, k int) int {
    flatArray := make([]int, len(matrix) * len(matrix[0]))
    
    for idx, row := range matrix {
        for j, col := range row {
            flatArray[idx * len(row) + j] = col
        }
    }
    
    sort.Ints(flatArray)
    
    return flatArray[k - 1]
}

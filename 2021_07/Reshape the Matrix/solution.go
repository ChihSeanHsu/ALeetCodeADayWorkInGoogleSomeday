func matrixReshape(mat [][]int, r int, c int) [][]int {
    if r * c != len(mat) * len(mat[0]) {
        return mat
    }
    
    result := make([][]int, r)
    for i := 0;i < r;i++ {
        result[i] = make([]int, c)
    }

    flatArray := make([]int, len(mat) * len(mat[0]))
    for rowIndex, row := range mat {
        for colIndex, col := range row {
            flatArray[rowIndex * len(row) + colIndex] = col
        }
    }

    for i := 0; i < r; i++ {
        for j := 0; j < c; j++ {
            result[i][j] = flatArray[i * c + j]
        }
    }
    return result
}

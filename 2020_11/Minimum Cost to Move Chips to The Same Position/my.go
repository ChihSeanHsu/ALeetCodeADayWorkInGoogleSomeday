func minCostToMoveChips(position []int) int {
    odd, even := 0, 0
    for _, i := range position {
        if (i % 2 == 0) {
            even++
        } else {
            odd++
        }
    }
    if odd > even {
        return even
    } else {
        return odd
    }
}

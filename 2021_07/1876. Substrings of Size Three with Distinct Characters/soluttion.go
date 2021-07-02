func countGoodSubstrings(s string) int {
    result := 0
    for i := 0; i < len(s) - 2 ; i++ {
        mapping := make(map[string]bool)
        for j := 0; j < 3; j++ {
            mapping[s[i + j:i + j + 1]] = true
        }
        if len(mapping) == 3 {
            result += 1
        }
    }
    return result
}

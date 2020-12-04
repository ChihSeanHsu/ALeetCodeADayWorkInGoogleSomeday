func kthFactor(n int, k int) int {
    count := 0
    now := 1
    for (now <= n) {
        if (n % now == 0) {
            count++
            if (count == k) {
                return now
            }
        }
        now++
    }
    return -1
}

func smallestDivisor(nums []int, threshold int) int {
    lower, upper := 1, max(nums)
    for lower < upper {
        mid := (lower + upper) >> 1
        res := getDivSum(nums, mid)
        if res > threshold {
            lower = mid + 1
        } else {
            upper = mid
        }
    }
    return lower
}

func max(nums []int) int {
    result := nums[0]
    for _, i := range nums {
        if result < i {
            result = i
        }
    }
    return result
}

func getDivSum(nums []int, mid int) int {
    res := 0
    for _, i := range nums {
        if i % mid == 0 {
            res += i / mid
        } else {
            res += (i / mid) + 1
        }
    }
    return res
}

func searchRange(nums []int, target int) []int {
    switch {
        case len(nums) == 0:
            return []int{-1, -1}
        case len(nums) == 1 && nums[0] == target:
            return []int{0, 0}
        case len(nums) == 1 && nums[0] != target:
            return []int{-1, -1}
    }
    result := []int{-1, -1}
    
    start := 0
    end := len(nums) - 1
    mid := 0
    find := false
    for start <= end {
        mid = (start + end) / 2
        if nums[mid] == target {
            find = true
            break
        } else if nums[mid] > target {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    
    if find {
        left := mid
        right := mid
        for left > -1 && nums[left] == target {
            left--
        }
        for right < len(nums) && nums[right] == target {
            right++
        }
        result[0] = left + 1
        result[1] = right - 1
    }
    
    return result
    
}

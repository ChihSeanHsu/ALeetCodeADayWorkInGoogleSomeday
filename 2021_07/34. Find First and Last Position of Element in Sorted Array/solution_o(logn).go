func biscetLeft(nums []int, target int) int {
    start := 0
    end := len(nums) - 1
    for start <= end {
        mid := (start + end) / 2
        if nums[mid] >= target {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }

    return start
}

func biscetRight(nums []int, target int) int {
    start := 0
    end := len(nums) - 1
    for start <= end{
        mid := (start + end) / 2
        if nums[mid] > target {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }

    
    return end
}


func searchRange(nums []int, target int) []int {
    left := biscetLeft(nums, target)
    right := biscetRight(nums, target) 
    if left <= right {
        return []int{left, right}
    } else {
        return []int{-1, -1}
    }
    
}
    

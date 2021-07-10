// prepare a subseqence by ourselves
// and then use binarysearch to find do we need insert new element in sub or not

func lengthOfLIS(nums []int) int {
    sub := []int{}
    sub = append(sub, nums[0])
    for i := 1; i < len(nums); i++ {
        if nums[i] > sub[len(sub) - 1] {
            sub = append(sub, nums[i])
        } else {
            idx := binarySearch(sub, nums[i])
            sub[idx] = nums[i]
        }
    }
    return len(sub)
}

func binarySearch(seq []int, target int) int {
    start := 0
    end := len(seq) - 1
    for start < end {
        mid := (start + end) / 2
        if seq[mid] == target {
            return mid
        } else if seq[mid] > target {
            end = mid
        } else {
            start = mid + 1
        }
    }
    
    return start
}

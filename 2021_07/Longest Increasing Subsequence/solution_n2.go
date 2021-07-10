func lengthOfLIS(nums []int) int {
    dp := make([]int, len(nums))
    for i := 0; i< len(dp); i++ {
        dp[i] = 1
    }
    
    for i := 0; i < len(nums); i++ {
        for j := 0; j < i;j++ {
            if nums[i] > nums[j] {
                tmp := dp[j] + 1
                if dp[i] < tmp {
                    dp[i] = tmp
                }
            }
        }
    }
    
    result := 0 
    for _, count := range dp {
        if result < count {
            result = count
        }
    }
    return result
}

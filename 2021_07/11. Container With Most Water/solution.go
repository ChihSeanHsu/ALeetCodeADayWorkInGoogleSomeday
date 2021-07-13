func maxArea(height []int) int {
    left := 0
    right := len(height) - 1
    result := 0
    for left < right {
        l := right - left
        h := height[left]
        if height[left] > height[right] {
            h = height[right]
        }
        contain := l * h
        if result < contain {
            result = contain
        }
        
        if height[left] > height[right] {
            right--
        } else {
            left++
        }
    }
    return result
}

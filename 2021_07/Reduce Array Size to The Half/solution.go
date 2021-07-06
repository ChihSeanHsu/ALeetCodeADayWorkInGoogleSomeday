import "sort"


func minSetSize(arr []int) int {
    counter := make(map[int]int)
    n := len(arr)
    half := n / 2
    result := 0
    
    for _, i := range arr {
        counter[i]++
    }
    
    countSorted := []int{}
    for _, value := range counter {
        countSorted = append(countSorted, value)
    }
    sort.Ints(countSorted)

    for i := len(countSorted) - 1; i >= 0 ; i-- {
        n -= countSorted[i]
        result++
        if n <= half {
            break
        }
    }
    
    return result
}

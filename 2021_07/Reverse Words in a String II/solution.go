func swap(s []byte, start int, end int) {
    for start < end {
        s[start], s[end] = s[end], s[start]
        start++
        end--
    }
}

func reverseWords(s []byte)  {
    start := 0
    end := len(s) - 1
    swap(s, start, end)
    
    start = 0
    for start < len(s) {
        end = start
        for end < len(s) && s[end] != ' '{
            end++
        }
        swap(s, start, end - 1)
        start = end + 1
    }
}

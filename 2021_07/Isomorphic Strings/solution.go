func isIsomorphic(s string, t string) bool {
    sTotMapping := make(map[byte]byte)
    tVisiter := make(map[byte]bool)
    for i := 0; i < len(s); i++ {
        if b, ok := sTotMapping[s[i]]; ok {
            if b != t[i] {
                return false
            }
        } else {
            if tVisiter[t[i]] {
                return false
            } else {
                sTotMapping[s[i]] = t[i]
                tVisiter[t[i]] = true
            }
        }
        
    }

    return true
    
}

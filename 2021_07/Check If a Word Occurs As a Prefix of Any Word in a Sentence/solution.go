import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
    for i, word := range strings.Split(sentence, " ") {
        if len(word) < len(searchWord) {
            continue
        }
        
        if searchWord == word[:len(searchWord)] {
            return i + 1
        }
    }
    return -1
}

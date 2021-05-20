from collections import deque, defaultdict
from string import ascii_lowercase 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        result = 0
        word_set = set(wordList)
        if not endWord in word_set:
            return result
        
        queue = deque()
        queue.append(beginWord)
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result + 1
                
                for idx in range(len(word)):
                    new_word = word
                    for c in ascii_lowercase:
                        new_word = new_word[:idx] + c + new_word[idx + 1:]
                        if new_word in word_set:
                            word_set.remove(new_word)
                            queue.append(new_word)
                            
            result += 1
        
        return 0
    

                    

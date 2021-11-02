class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        store = []
        space_count = 0
        char_count = 0
        result = []
        for word in words:
            if space_count + char_count + len(word) > maxWidth:
                interval = len(store) - 1
                if interval > 0:
                    total_space = maxWidth - char_count
                    big_interval_count = total_space % interval
                    interval_space = total_space // interval

                    tmp = ""
                    for idx, i in enumerate(store):
                        tmp += i
                        if idx <= big_interval_count - 1:
                            tmp += " " * interval_space + " "
                        elif idx < interval:
                            tmp += " " * interval_space
                else:
                    tmp = " ".join(store)
                    tmp = tmp.ljust(maxWidth)

                result.append(tmp)
                space_count = 0
                char_count = 0
                store = []
                
            
            space_count += 1
            char_count += len(word)
            store.append(word)
            
        if store:
            tmp = " ".join(store)
            tmp = tmp.ljust(maxWidth)
            result.append(tmp)
        return result
            
                    

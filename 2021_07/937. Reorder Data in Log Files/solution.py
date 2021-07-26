class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_array = []
        digit_array = []
        
        for log in logs:
            splitted_log = log.split(" ", 1)
            
            if splitted_log[1][0].isdigit():
                digit_array.append(log)
            else:
                for idx, l in enumerate(letter_array):
                    compare_splitted_log = l.split(" ", 1)
                    if splitted_log[1] == compare_splitted_log[1]:
                        if splitted_log[0] < compare_splitted_log[0]:
                            letter_array.insert(idx, log)
                            break
                        else:
                            idx += 1
                            letter_array.insert(idx, log)
                            break
                        
                    elif splitted_log[1] < compare_splitted_log[1]:
                        letter_array.insert(idx, log)
                        break
                else:
                    letter_array.append(log)
                
                
        return letter_array + digit_array
        

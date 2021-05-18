from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)
        for info in paths:
            path_and_file = info.split()
            path = path_and_file[0]
            for file in path_and_file[1:]:
                filename, content = file.split("(")
                content_dict[content].append(f"{path}/{filename}")
                
        return [value for key, value in content_dict.items() if len(value) > 1]
        
        

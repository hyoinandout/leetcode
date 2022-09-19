class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        answer = []
        dict_content = dict()
        for path in paths:
            chunks = path.split()
            file_path = chunks[0]
            for chunk in chunks[1:]:
                filename, content = chunk.split('(')
                content = content[:-1]
                full_filename = file_path + '/' + filename
                try:
                    dict_content[content].append(full_filename)
                except:
                    dict_content[content] = [full_filename]
        for key in dict_content.keys():
            if len(dict_content[key]) > 1:
                answer.append(dict_content[key])
        return answer
                    
                
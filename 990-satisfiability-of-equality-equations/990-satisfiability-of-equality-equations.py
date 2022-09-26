class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key=lambda x: x[1], reverse=True)
        print(equations)
        alphabets = [i for i in range(26)]
        
        def findParent(son: int):
            while alphabets[son] != son:
                son = alphabets[son]
            return son
        
        def unionParent(a:int, b:int):
            a = findParent(a)
            b = findParent(b)
            
            if a < b:
                alphabets[b] = a
            else:
                alphabets[a] = b
        
        for equation in equations:
            if equation[1] == "=":
                unionParent(ord(equation[0]) - 97,ord(equation[3]) - 97)
            else:
                if equation[0] < equation[3]:
                    if findParent(ord(equation[3]) - 97) == findParent(ord(equation[0]) - 97):
                        return False
                else:
                    if findParent(ord(equation[0]) - 97) == findParent(ord(equation[3]) - 97):
                        return False
        print(alphabets)
        return True
            
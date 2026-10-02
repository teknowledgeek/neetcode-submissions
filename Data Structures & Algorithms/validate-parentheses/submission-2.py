from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if not s :
            return True
        
        def findPair(s : str) -> str:
            if s == '[':
                return "]"
            if s == '{':
                return "}"
            if s == '(':
                return ")"
        i = 0
        
        queue = deque()
        while i < len(s):
            if s[i] in ['[', '{', '('] :
                queue.append(s[i])

            if s[i] in [']', '}', ')'] :
                if queue: 
                    open = queue.pop()
                    if findPair(open) != s[i]:
                        return False
                else:
                    return False
            i+=1
        if queue:
            return False
        else: 
            return True        

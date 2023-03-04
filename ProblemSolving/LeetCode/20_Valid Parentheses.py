### Runtime: 66.44%, Memory:60.64%

class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"}":"{", ")":"(", "]":"["}

        brace_stack = []
        for ch in s:
            if ch in braces.keys():
                if len(brace_stack)> 0 and brace_stack[-1] == braces[ch]:
                    del brace_stack[-1]
                else:
                    return False
            elif ch in braces.values():
                brace_stack.append(ch)
            else:
                return False

        if len(brace_stack) > 0:
            return False
        return True

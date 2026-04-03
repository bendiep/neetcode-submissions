class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case: Odd length string is always invalid
        if len(s) % 2 != 0:
            return False

        open_brackets = ["(", "{", "["]
        open_stack = []
        result = True

        for bracket in s:
            # Append OPEN brackets ON stack
            if bracket in open_brackets:
                open_stack.append(bracket)
            else:
                # Edge case: Stack empty, but a close bracket still remains
                if len(open_stack) == 0:
                    result = False
                    break
                
                # Pop CLOSED brackets OFF stack
                if open_stack[-1] == "(" and bracket == ")":
                    open_stack.pop()
                elif open_stack[-1] == "{" and bracket == "}":
                    open_stack.pop()
                elif open_stack[-1] == "[" and bracket == "]":
                    open_stack.pop()
                else: # Edge case: Stack not empty, but close bracket didn't match
                    result = False
                    break
        
        # Edge case: left over open brackets
        if len(open_stack) != 0:
            result = False

        return result
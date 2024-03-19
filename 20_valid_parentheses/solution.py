from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        # if there are an uneven number of characters, return false
        if len(s) % 2 != 0 or not s:
            return False

        terminating_map = {")": "(", "]": "[", "}": "{"}
        stack = deque()

        for char in s:
            if char in terminating_map.keys():
                # char is a closing parentheses, check for associated opening paren
                if stack:
                    top_val = stack[0]
                    if terminating_map[char] == top_val:
                        stack.popleft()
                    else:
                        # incorrect opening parentheses
                        return False
                else:
                    # expected an opening parentheses but the stack was empty
                    return False
            else:
                # char is an opening parentheses
                stack.appendleft(char)

        return len(stack) == 0


solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("}["))

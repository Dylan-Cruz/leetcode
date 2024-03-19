from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        # if there are an uneven number of characters, return false
        if len(s) % 2 != 0:
            return False

        terminating_map = {')': '(', ']': '[', '}': '{'}
        
        queue = deque()

        for char in s:
            if char in terminating_map.keys():
                # if the top_val is the expected opening paren
                # pop it off the queue
                top_val = deque[0]
                if terminating_map[char] == top_val:
                    deque.popleft()
                else: 
                    # an invalid opening parentheses 
                    return False
            else:
                queue.appendleft(char)
        
        if not queue:
            # if queue isn't empty
            return False

        return True
        

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
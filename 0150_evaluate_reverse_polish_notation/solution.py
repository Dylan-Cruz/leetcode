from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operator_set = set(["+", "-", "*", "/"])
        operand_stack = []
        for token in tokens:
            if token in operator_set:
                second_op = operand_stack.pop()
                first_op = operand_stack.pop()

                if token == "+":
                    result_op = first_op + second_op
                elif token == "-":
                    result_op = first_op - second_op
                elif token == "*":
                    result_op = first_op * second_op
                else:
                    # token is /
                    result_op = int(
                        first_op / second_op
                    )  # fp math, int truncates toward zero while floor division rounds to nearest whole number

                operand_stack.append(result_op)
            else:
                operand_stack.append(int(token))

        # the last value on the stack is the answer
        return operand_stack.pop()


solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))
print(solution.evalRPN(["4", "13", "5", "/", "+"]))
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)

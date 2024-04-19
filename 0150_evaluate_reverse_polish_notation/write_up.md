# Write Up

## Intuition

This problem can be solved pretty easily with a stack at first glance. The workflow is as follows:

```
for each token in tokens
    if operand
        push to stack
    else
        pop two values off stack
        perform operation
        push result

if rpn list was valid, stack will contain one element, the result
```

A few additional points worth mentioning, the order of the operands that get popped matters in terms of division and subtraction. The second value you pop is the leading term in the next operation. It behooves you to parse the tokens to ints as you push operands to the stack so everything is an integer.

## Approach

This problem can be solved pretty easily with a stack at first glance. The workflow is as follows:

```
for each token in tokens
    if operand
        push to stack
    else
        pop two values off stack
        perform operation
        push result

if rpn list was valid, stack will contain one element, the result
```

A few additional points worth mentioning, the order of the operands that get popped matters in terms of division and subtraction. The second value you pop is the leading term in the next operation. It behooves you to parse the tokens to ints as you push operands to the stack so everything is an integer. Floor division in python rounds to the nearest whole number not towards 0 like in java while the Int constructor rounds toward 0. I missed an edge case where a single value could be pushed to the stack and is a valid expression which surfaced I should've been parsing to an int when pushing an operand from the input

## Time Complexity

- O(N)
- Each token is visited once

## Space Complexity

- O(N)
- if X is the number of operations present, there are a max of X+1 operands since the result is considered an operand.

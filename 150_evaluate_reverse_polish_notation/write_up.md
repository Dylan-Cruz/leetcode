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
This ended up being the valid approach and while I was confident in my code on first write, there were several gotchas I hadn't accounted for. Here's a list of things I learned or learned that I need to think about:
1. floor division in python rounds to the nearest whole number not towards 0 like in java. 
2. I forgot to parse the the token to an integer. In languages I'm currently working with, it's implicit
3. I tried to use the is operator in the if clauses but that's only for identity not equality
4. I missed an edge case where a single value could be pushed to the stack and is a valid expression which surfaced I should've been parsing to an int when pushing an operand from the input

## Time Complexity
- O(N)
- Each token is visited once

## Space Complexity
- O(N)
- if X is the number of operations present, there are a max of X+1 operands since the result is considered an operand. 
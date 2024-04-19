# Write Up

## Approach
The approach here is to use a stack to maintain a list of opening parentheses as they're encountered and to pop them off the stack when we encounter an associated closing parentheses. If at any point a closing parentheses is encountered and the stack is empty or contains an opening parentheses other than it's associated member, return false. Finally, only return true if the stack is empty. A value could be left there in the event there was one more opening paren than closing. 

I was pretty happy with this solution on the first try beating 77% of users in runtime. I was able to tweak it slightly by changing my last return to check for `len(stack) == 0`. This improved the runtime by 7 ms beating 97% of users. I could have used a regular list instead of a deque and just appended and popped from the right but conceptually I like to picture a stack operating from the left. 

## Time Complexity
- O(N)
- Each char in the string is inspected once. The remaining operations are constant time

## Space Complexity
- O(N)
- A stack is used to maintain a list of opening parentheses. In the worst case where all characters are opening parentheses it'd be N characters long. The map of terminating characters to opening ones is constant additional space. 

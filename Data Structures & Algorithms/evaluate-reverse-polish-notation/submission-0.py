class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second-first)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(t))
        return stack[0]
# 괄호
import sys

T = int(input())

for _ in range(T):
    str = sys.stdin.readline()

    stack = []

    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[':
            stack.append(str[i])
        elif stack and stack[-1] == '(' and str[i] == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and str[i] == ']':
            stack.pop()
        elif str[i] == ')' or str[i] == ']':
            stack.append(str[i])
            break
    
    if not stack:
        print("YES")
    else:
        print("NO")
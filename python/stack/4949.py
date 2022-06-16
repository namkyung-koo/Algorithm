# 균형잡힌 세상
import sys

while True:
    # 자동으로 붙는 개행문자를 rstrip() method로 제거
    str = sys.stdin.readline().rstrip()
    
    if str == '.':
        break

    stack = []

    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[':
            stack.append(str[i])
        elif stack and stack[-1] == '[' and str[i] == ']':
            stack.pop()
        elif stack and stack[-1] == '(' and str[i] == ')':
            stack.pop()
        elif str[i] == ')' or str[i] == ']':
            stack.append(str[i])
            break
    
    if not stack:
        print("yes")
    else:
        print("no")
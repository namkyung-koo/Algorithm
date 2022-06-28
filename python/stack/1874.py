# 스택 수열
n = int(input())

stack = []

i = 1

cnt = 0

comp = 0

def peek_stack(stack):
    if stack:
        return stack[-1]

while True:
    num = int(input())
    if comp < num:
        while comp < num:
            stack.append(i)
            print('+')
            comp = i
            i += 1
    stack.pop()
    print('-')
    cnt += 1
    if cnt == n:
        break
    
    
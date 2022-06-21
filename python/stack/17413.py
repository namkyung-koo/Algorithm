# 단어 뒤집기 2
S = input()

stack = []

res = ''

i = 0

while range(len(S)):
    while chr(48) <= S[i] <= chr(57) or chr(97) <= S[i] <= chr(122):
        stack.append(S[i])
        if i == len(S) - 1:
            break
        i += 1
    while stack:
        res += stack.pop()
    if S[i] == '<':
        while S[i] != '>':
            res += S[i]
            if i == len(S) - 1:
                 break
            i += 1
        res += S[i]
    if S[i] == ' ':
        res += S[i]
    if i == len(S) - 1:
        break
    i += 1
print(res)
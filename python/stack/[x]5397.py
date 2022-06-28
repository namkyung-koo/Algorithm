# 키로거
T = int(input())

for _ in range(T):
    tmp = []
    pw = []
    stack = []
    cur = -1

    tmp = input()
    for i in range(len(tmp)):
        if stack and (chr(48) <= tmp[i] <= chr(57) or chr(65) <= tmp[i] <= chr(90) or chr(97) <= tmp[i] <= chr(122)):
            pw.insert(cur, tmp[i])
            if cur < len(tmp) - 1:
                cur += 1

        if not stack and (chr(48) <= tmp[i] <= chr(57) or chr(65) <= tmp[i] <= chr(90) or chr(97) <= tmp[i] <= chr(122)):
            pw.append(tmp[i])
            if cur < len(tmp) - 1:
                cur += 1

    # pw가 빈 리스트가 아닐 때만 커서의 이동을 인식한다. 짝을 맞추기 위해 '<'을 stack에 넣는다.
        if pw and tmp[i] == '<':
            if stack and cur > 0:
                cur -= 1
            stack.append(tmp[i])

        if stack and tmp[i] == '>':
            stack.pop()
        
        if pw and tmp[i] == '-':
            pw.pop(cur)
            cur -= 1

    print(''.join(pw))

# '-'를 만났을 때 pop()을 실행하기 위해, 배열 pw를 활용한다. 이후에 str로 바꿔서 프린트할 것임.
# cur이라는 정수형 변수는 인덱스 접근을 도와주고 '<'가 나왔을 때 stack에 쌓는다.
# '>'는 '<'가 스택에 있을 때만 즉, 짝을 맞춰서만 실행할 수 있다.
# '<'는 cur -= 1, '>'은 cur += 1
# pw.insert(idx, tmp[i])로 중간에 삽입 가능
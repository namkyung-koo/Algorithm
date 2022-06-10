# 하노이 탑 이동 순서
N = int(input())

def hanoi(n, From, by, to):
    if n == 1:
        print("{} {}".format(From, to))
    else:
        hanoi(n - 1, From, to, by)
        print("{} {}".format(From, to))
        hanoi(n - 1, by, From, to)

print(2**N - 1)
hanoi(N, 1, 2, 3)
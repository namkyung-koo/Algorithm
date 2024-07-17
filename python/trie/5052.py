'''
[ 전화번호 목록 ]

< 풀이과정 >
trie 자료구조의 적용
'''

import sys

class Trie(object):
    def __init__(self):
        self.end = False
        self.passed = False
        self.children = [None] * 10

    def insert(self, string, index):
        
        if self.end:
            return False

        if index == len(string):
            self.end = True
            if self.passed:
                return False
            else:
                return True
            
        next_index = int(string[index])
        if self.children[next_index] is None:
            self.children[next_index] = Trie()
            self.passed = True

        return self.children[next_index].insert(string, index + 1)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    trie = Trie()
    answer = ""

    for _ in range(n):
        number = sys.stdin.readline().strip()
        if trie.insert(number, 0) == False:
            answer = "NO"

    if answer == "":
        answer = "YES"
    print(answer)
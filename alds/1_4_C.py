import sys

input = sys.stdin.readline


class Dictionary:
    M = 1046527
    T = [None] * M

    def h1(self, key):
        return key % self.M

    def h2(self, key):
        return 1 + (key % (self.M - 1))

    def h(self, key, i):
        return (self.h1(key) + i * self.h2(key)) % self.M

    def insert(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self.T[j] is None:
                self.T[j] = key
                return j
            else:
                i += 1

    def search(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self.T[j] == key:
                return j
            elif self.T[j] is None or i >= self.M:
                return None
            else:
                i += 1


def getChar(string):
    table = str.maketrans({"A": "1", "C": "2", "G": "3", "T": "4"})
    return int(string.translate(table))


n = int(input())
dic = Dictionary()
for _ in range(n):
    com, string = input().split()
    string = getChar(string)
    if com[0] == "i":
        dic.insert(string)
    else:
        if dic.search(string):
            print("yes")
        else:
            print("no")

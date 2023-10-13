# Ref: https://atcoder.jp/contests/abc322/tasks/abc322_b

N, M = map(int, input().split())
S = input()
T = input()

isPre = S == T[:N]
isSuff = S == T[-N:]

if isPre and isSuff:
    print(0)
elif isPre:
    print(1)
elif isSuff:
    print(2)
else:
    print(3)

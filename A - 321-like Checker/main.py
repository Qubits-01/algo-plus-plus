# Ref: https://atcoder.jp/contests/abc321/tasks/abc321_a

N = [int(char) for char in input()]
curr_big_num = N.pop(0)

for num in N:
    if num < curr_big_num:
        curr_big_num = num
    else:
        print("No")
        exit()

print("Yes")

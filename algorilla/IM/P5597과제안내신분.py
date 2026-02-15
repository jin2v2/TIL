# 1~30 중에 없는 수 구하기.
lst = list(range(1, 31))

for i in range(28):
    num = int(input())
    lst.remove(num)

for j in lst:
    print(j)
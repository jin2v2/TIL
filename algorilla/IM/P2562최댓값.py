lst = []
for _ in range(9):
    arr = int(input())
    lst.append(arr)

print(max(lst))
print(lst.index(max(lst))+1)
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    
    tot = sum(arr[1:])
    per = arr[0]
    
    avg = tot / per

    stu = 0

    for i in arr[1:]:
        if i > avg:
            stu += 1

    print(f'{(stu / per * 100):.3f}%')
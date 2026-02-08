# # 부분 수열 판별
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    i = j = 0

    for i in range(N):
            if A[i] == B[j]:
                j += 1
            if j == M:
                break
    if j == M:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

# 입력값이 문자열 일때 비교
T = int(input())

for tc in range(1, T + 1):
    A = input().strip()   # 기준 문자열
    B = input().strip()   # 부분수열 후보

    j = 0  # B의 인덱스

    for i in range(len(A)):
        if j < len(B) and A[i] == B[j]:
            j += 1
        if j == len(B):
            break

    if j == len(B):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

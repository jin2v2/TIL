# 리스트2 연습문제 2
# 5x5 배열 입력
arr = [list(map(int, input().split())) for _ in range(5)]

# 델타 탐색 (상, 하, 좌, 우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

total = 0

for i in range(5):
    for j in range(5):
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 배열 범위 체크
            if 0 <= ni < 5 and 0 <= nj < 5:
                total += abs(arr[i][j] - arr[ni][nj])

print(total)
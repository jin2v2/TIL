N = 7
arr = [[0] * N for _ in range(N)]
# 사각 영역의 순회하기 위한 인덱스 생성
# 1. 사각 영역에서 좌상단, 우하단 좌표 확인
r1, c1 = 2, 2
r2, c2 = 4, 5
for r in range(r1, r2 + 1):
    for c in range(c1, c2+1):
        arr[r][c] = 1

# 2. 좌상단, 높이(행크기), 너비(열크기)
r1, c1 = 2, 2 # 좌상단
H, W = 3, 4 # 높이, 너비

# 행 우선 좌표 생성
# 행 값의 범위
for r in range(r1, r1+H):
    for c in range(c1, c1+W-1):
        arr[r][c] = 2 # 사각 영역이 2로 채워짐.

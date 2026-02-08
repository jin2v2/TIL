# 12388 색칠하기 확인용
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 직사각형 영역 칠하기 (r1~r2, c1~c2 포함)
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += color

    # 보라색(1+2=3) 칸 세기
    purple = 0
    for r in range(10):
        for c in range(10):
            if board[r][c] == 3:
                purple += 1

    print(f"#{tc} {purple}")
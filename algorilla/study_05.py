#풍선팡2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(M):
            balloon = arr[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    balloon += arr[nx][ny]
            if max_v < balloon:
                max_v = balloon
                
    print(f'#{tc} {max_v}')
#

# 1954. 달팽이
T=int(input())
for test_case in range(1,T+1):
    N= int(input())
    arr = [[0]* N for _ in range(N)] #배열 생성
    x = 0
    y = 0
    d = 0 #방향
    dx = [0, 1, 0, -1] #동남서북 순
    dy = [1, 0, -1, 0]
    count = 1

    while count <= N*N: #count 수가 N*N 범위를 안 넘는 동안 while문 실행
        arr[x][y] = count # 시작점(기준점) = count

        if count == N*N: #만약 count가 범위 값과 같아진다면 break
            break

        nx,ny = x+dx[d], y+dy[d] #전진하는 값 (다음 목적지) 확인
        if not (0<=nx<N and 0<=ny<N) or arr[nx][ny] !=0: 
            #만약 앞에 갈 곳이 nx,ny값이 범위를 넘어가거나 count가 이미 존재하다면
            d = (d+1) % 4 #오른쪽으로 90도 회전(남쪽)
            nx,ny = x+dx[d], y+dy[d] #전진하는 값(다음 목적지) 확인

        x,y = nx, ny #x,y 값 갱신 : 앞으로 전진함
        count += 1 #count 값 추가
    print(f'#{test_case}')
    for result in arr: #arr 값이 리스트이므로 값 하나씩 추출
        print(*result) #언패킹 후 출력
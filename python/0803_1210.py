T = 10
N = 100

for tc in range(1, T+1):
    int(input()) # tc번호 입력 처리 - 저장은 안함
    ladder = [list(map(int, input().split())) for _ in range(N)]

    # 내가 위치를 직접 움직여야 한다.
    r = 99
    c = -1 #마지막 행 검사해서 2인곳을 찾을거다.

    # 2라고 표시된 곳을 마지막 줄에서 찾기
    # for i in ladder[99]:
    #     if i == 2:
    #         c += 1
    #         break
    #     c += 1
    for i in range(N):
        if ladder[99][i] == 2: # 옆에 번호 눌러서
            c = i

    # 상하방향으로 가는데 중간에 좌우 방향에 길이 있으면 좌우부터
    # 올라온길은 0으로 흔적남겨서 가지 못하게 만듦
    dr = [0, 0, -1] #좌 => 우 => 상 순서로 탐색
    dc = [-1, 1, 0]

    # 행 번호가 0보다 크면 아직 시작점이 아니니까
    # 계속 이동
    while r > 0:
        # 이동할 때마다 좌=> 우=> 상 순서로 탐색
        for d in range(3):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치가 유효한 인덱스인지 검사
            # 길이 있어야 갈 수 있다.
            if 0<=nr<N and 0<= nc <N and ladder[nr][nc] == 1:
                # 갈 수 있으면 간다.
                # 현재위치를 최신화
                r = nr
                c = nc
                # 내가 왔던 길은 다시 보지 않도록 0으로 바꾼다.
                ladder[r][c] = 0
                # 길을 찾았으니까 다음방향 볼 필요 xx
                break
    print(c)




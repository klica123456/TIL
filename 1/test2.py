T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    d = 0
    r, c = 0, 0
    dr = [0, 1, 0, -1]  # 상하좌우
    dc = [1, 0, -1, 0]
    for i in range(1, (N*N)+1):
        snail[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0: # snail[nr][nc]먼저 쓰면 nr, nc가 범위를 벗어나 index에러가 일어날 수 있음
            r, c = nr, nc
        else:
            d = d + 1 if d < 3 else 0
            r = r + dr[d]
            c = c + dc[d]
    for i in snail:
        print(*i)

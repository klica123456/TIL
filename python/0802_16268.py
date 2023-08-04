t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    lis = [list(map(int, input().split())) for _ in range(N)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    max_val = 0
    for i in range(N):
        for j in range(M):
            num = lis[i][j]
            for k in range(4):
                ni = i + dj[k]
                nj = j + di[k]
                if 0 <= ni < N and 0 <= nj < M:
                    num += lis[ni][nj]
            if num > max_val:
                max_val = num
    print(f'#{tc} {max_val}')

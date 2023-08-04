t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split()) # input().split()하면 list가 형성되서 int로 못 묶음 map을써줘야됨
    lis = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for j in range(N-M+1):
        for k in range(N-M+1):
            num = 0
            for i in range(M):
                for p in range(M):
                    num += lis[j+i][k+p]
            if num > max_val:
                max_val = num
    print(f'#{tc} {max_val}')



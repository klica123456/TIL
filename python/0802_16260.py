t = int(input())

for tc in range(1, t+1):
    N = int(input())
    T = [list(map(int, input().split())) for _ in range(N)]
    lis = list([0]*10 for _ in range(10))
    T_len = len(T)
    count_val = 0
    for i in T:
        r1 = i[0]
        c1 = i[1]
        r2 = i[2]
        c2 = i[3]
        for a in range(r1, r2+1):
            for b in range(c1, c2+1):
                lis[a][b] += i[4]

    for i in range(10):
        for j in range(10):
            if lis[i][j] == 3:
                count_val += 1
    print(f'#{tc} {count_val}')



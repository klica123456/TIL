T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lis = [list(map(int, input().split())) for _ in range(Q)]
    ans_lis = [0] * N
    for i in range(1, Q+1):
        # print(lis[i-1][0], lis[i-1][1])
        for k in range(lis[i-1][0]-1, lis[i-1][1]):
            ans_lis[k] = i
    print(f'#{tc}', *ans_lis)



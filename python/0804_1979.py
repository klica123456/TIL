import sys

sys.stdin = open('0804_1979.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lis = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # print(lis)
    dr = []
    dc = []
    a = 0
    for i in range(N):
        for j in lis[i]:
            if j == 1:
                a += 1
            else:
                dr.append(a)
                a = 0
        dr.append(a)
        a = 0
    # print(dr)

    b = 0
    for i in range(N):
        for j in range(N):
            if lis[j][i] == 1:
                b += 1
            else:
                dc.append(b)
                b = 0
        dc.append(b)
        b = 0
    # print(dc)
    for i in dr:
        if i == K:
            ans += 1

    for i in dc:
        if i == K:
            ans += 1

    print(f'#{tc} {ans}')




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    K = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stp = [int(input()) for _ in range(P)]
    l = [0] * P
    a, b = 0, 0
    for i in K:
        for j in range(len(stp)):
            if len(i) == 1:
                if i[0] == stp[j]:
                    l[j] += 1
            else:
                for k in range(i[0], i[1]+1):
                    if k == stp[j]:
                        l[j] += 1
    print(f'#{tc}', *l)

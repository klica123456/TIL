T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    a_count = list(map(int, input().split()))
    count = K
    ans = 0
    a = -1
    F = 0

    for i in range(0, N+1):
        if i > a:
            if a + count == N-1:
                break
            for j in a_count:
                if j in range(i, i+count+1):
                    a = j
        if i == a:
            count = K
            ans += 1
        count -= 1
        if count < -1:
            F = 1
            break

    if F:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {ans}')


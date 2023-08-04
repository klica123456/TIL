T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    lis = list(map(int, input().split()))
    q = -1
    for i in range(N):
        q += 1
        minIdx = i
        for j in range(i + 1, N):
            if q % 2 == 1:
                if lis[minIdx] > lis[j]:
                    minIdx = j
            if q % 2 == 0:
                if lis[minIdx] < lis[j]:
                    minIdx = j
        lis[i], lis[minIdx] = lis[minIdx], lis[i]

    print(f'#{test_case}', *(lis[:10]))
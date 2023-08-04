T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    print(f'#{test_case} {li[-1] - li[0]}')







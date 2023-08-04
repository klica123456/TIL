T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    lis = list(input().split() for _ in range(a))
    kills = []
    for i in range(a-b+1):
        for n in range(a-b+1):
            k = 0
            for j in range(b):
                for p in range(b):

                    k += int(lis[j+i][p+n])

            kills.append(k)
    print(f"#{test_case} {max(kills)}")


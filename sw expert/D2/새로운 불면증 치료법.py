T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())
    lis = []
    p = []
    i = 1
    while len(p) < 10:
        b = i * a
        i += 1
        k = list(str(b))
        lis += k

        p = set(lis)

    print(f"#{test_case} {b}")
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = 0
    o = 0
    a = int(input())
    b = list(input().split() for _ in range(a))
    for i in b:
        if int(i[0]) == 1:
            k = (int(i[1]) + k)
            o += k

        elif int(i[0]) == 2:
            k = (-int(i[1]) + k)
            if k < 0:
                k = 0
            o += k
        else:
            o += k

    print(f"#{test_case} {o}")
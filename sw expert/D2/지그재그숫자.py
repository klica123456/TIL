T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())
    k = 0
    for i in range(1, a+1):
        if i%2 == 0:
            k -= i
        else:
            k += i
    print(f"#{test_case} {k}")

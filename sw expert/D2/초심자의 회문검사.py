import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = list(input())
    k = []
    p = []
    for i in range(math.ceil(len(a)/2)):
        k.append(a[i])
    for i in range(math.trunc(len(a)/2), len(a)):
        p.append(a[i])
    p.reverse()
    if k == p:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")



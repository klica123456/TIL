T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:30}
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0
    f = a[m1] - d1 + 1
    if m1 != m2:
        for i in range(m1+1, m2):
            print(i)
            ans += a[i]
        print(f"#{test_case} {ans+f+d2}")
    else:
        print(f"#{test_case} {d2-d1+1}")
    

    


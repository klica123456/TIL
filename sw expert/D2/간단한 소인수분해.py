T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = [2, 3, 5, 7, 11]
    k = int(input())
    lis = []
    for i in a:
        l = 0
        while k%i == 0:
            k = k/i
            l += 1
        lis.append(l)
    print(f"#{test_case}", end = ' ')
    print(*lis)
        
        

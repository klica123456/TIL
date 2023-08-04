T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    lis1 = [A, B]
    lis = [0, 0]
    for i in range(2):
        start = 0
        end = P
        while start <= end:
            lis[i] += 1
            middle = int((start+end)/2)
            if middle == lis1[i]:
                break
            elif middle > lis1[i]:
                end = middle
            else:
                start = middle

    if lis[0] > lis[1]:
        print(f'#{test_case} B')
    elif lis[0] == lis[1]:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} A')
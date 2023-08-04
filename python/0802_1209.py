T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    lis = [list(map(int, input().split())) for _ in range(100)]
    ans_lis = []
    x1 = 0
    x2 = 0
    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += lis[i][j]
            col += lis[j][i]
        ans_lis.append(row)
        ans_lis.append(col)

    for k in range(100):
        x1 += lis[0+k][0+k]
        x2 += lis[0+k][99-k]
    ans_lis.append(x1)
    ans_lis.append(x2)
    temp = 0
    for i in ans_lis:
        if temp == 0 or temp < i:
            temp = i
    print(f'#{tc} {temp}')
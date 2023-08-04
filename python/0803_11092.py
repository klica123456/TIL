T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lis = list(map(int, input().split()))
    temp1 = lis[0]
    temp2 = lis[0]
    a = 0
    b = 0
    for i in range(len(lis)):
        if temp1 > lis[i]:
            temp1 = lis[i]
            a = i
            # print(a)
        if temp2 <= lis[i]:
            temp2 = lis[i]
            b = i
        print(a, b)
    print(f'#{tc} {abs(b-a)}')
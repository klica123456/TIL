T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lis = list(str(input()))
    a = 0
    count = 0
    for i in lis:
        if i == '1':
            a += 1
        else:
            if count < a:
                count = a
            a = 0
    if count < a:
        count = a
    print(f'#{tc} {count}')


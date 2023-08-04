K = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    len_k = len(K)
    key = 0
    for i in range(1 << len_k):
        a = 0
        b = 0
        for j in range(len_k):
            if i & (1 << j):
                a += 1
                b += K[j]
        if a == A and b == B:
            key += 1
        else:
            key += 0
    if key >= 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
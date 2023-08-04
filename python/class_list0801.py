T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    for i in range(1, N):
        if arr[min_idx] >= arr[i]:
            min_idx = i
    print(min_idx)
    
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lis = list(map(int, input().split()))
    a = lis[0]
    count = 1
    ans = []
    for i in lis[1:]:
        if a < i:
            count += 1
            a = i
            # print(count)
        else:
            ans.append(count)
            a = i
            count = 1
    ans.append(count)
    for i in range(len(ans)):
        minIdx = i
        for j in range(i+1, len(ans)):
            if ans[minIdx] > ans[j]:
                minIdx = j
        ans[i], ans[minIdx] = ans[minIdx], ans[i]

    print(f'#{tc} {ans[len(ans)-1]}')


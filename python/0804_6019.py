T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    r = D/(A+B)
    ans = F*r
    print(f'#{tc} {ans}')

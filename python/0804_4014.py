import sys
sys.stdin = open('sample_input (8).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    lis_row = [list(map(int, input().split())) for _ in range(N)]
    lis_col = []
    ans = 0

    for i in range(N):
        a = []
        for j in range(N):
            a.append(lis_row[j][i])
        lis_col.append(a)

    for i in range(N):
        for j in range(N-1):
            if abs(lis_row[i][j]-lis_row[i][j+1]) > 1:
                del lis_row[i]
                lis_row.insert(i, '0')
                break

    for i in range(N):
        for j in range(N-1):
            if abs(lis_col[i][j] - lis_col[i][j+1]) > 1:
                del lis_col[i]
                lis_col.insert(i, '0')
                break

    for i in range(N):
        if len(lis_row[i]) == 1:
            continue
        key1 = 0
        for q in range(N-X, N):
            if lis_row[i][q] == lis_row[i][N - X]:
                key1 += 1
        if key1 != X:
            del lis_row[i]
            lis_row.insert(i, '0')
            continue
        a = lis_row[i][0]
        for j in range(1, N-X+1):
            count = 0
            if a > lis_row[i][j]:
                a = lis_row[i][j]
                for k in range(X):
                    if j+k > N-1:
                        break
                    if a == lis_row[i][j+k]:
                        count += 1
                if count != X:
                    del lis_row[i]
                    lis_row.insert(i, '0')
                    break
            if a < lis_row[i][j]:
                a = lis_row[i][j]
                for k in range(X):
                    if j-k-1 <0:
                        break
                    if lis_row[i][j-1] == lis_row[i][j - k - 1]:
                        count += 1
                if count != X-1:
                    del lis_row[i]
                    lis_row.insert(i, '0')
                    break

    for i in range(N):
        if len(lis_col[i]) == 1:
            continue
        key1 = 0
        for q in range(N - X, N):
            if lis_col[i][q] == lis_col[i][N - X]:
                key1 += 1
        if key1 != X:
            del lis_col[i]
            lis_col.insert(i, '0')
            continue
        a = lis_col[i][0]
        for j in range(1, N - X+1):
            count = 0
            if a > lis_col[i][j]:
                a = lis_col[i][j]
                for k in range(X):
                    if j+k > N-1:
                        break
                    if a == lis_col[i][j+k]:
                        count += 1
                if count != X:
                    del lis_col[i]
                    lis_col.insert(i, '0')
                    break
            if a < lis_col[i][j]:
                a = lis_col[i][j]
                for k in range(X):
                    if j-k-1 < 0:
                        break
                    if lis_col[i][j-1] == lis_col[i][j - k - 1]:
                        count += 1
                if count != X-1:
                    del lis_col[i]
                    lis_col.insert(i, '0')
                    break

    for i in lis_row:
        if len(i) == N:
            ans += 1

    for i in lis_col:
        if len(i) == N:
            ans += 1

    print(ans)




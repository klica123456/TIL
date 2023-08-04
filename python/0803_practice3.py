import random

T = int(input())
k = random.sample(range(1, T ** 2 + 1), T ** 2)
l = 0
lis = [[0] * T for _ in range(T)]

for i in range(T):
    for j in range(T):
        lis[i][j] = k[l]
        l += 1
a = []
for i in lis:
    print(*i)
    for j in i:
        a.append(j)

for i in range(len(a)):
    minIdx = i
    for j in range(i + 1, len(a)):
        if a[minIdx] > a[j]:
            minIdx = j
    a[i], a[minIdx] = a[minIdx], a[i]

snail = [[0] * T for _ in range(T)]


dr = [0, 1, 0, -1]  # 상하좌우
dc = [1, 0, -1, 0]
ni = 0
nj = 0
k = 0
# while True:
#     for i in range(4):
#         for j in range(T):
#             ni += dr[i]
#             nj += dc[i]
#             if 0 <= ni < T and 0 <= nj < T and snail[ni][nj] == 0:
#                     snail[ni][nj] = a[k]
#                     k += 1
#     if 0 not in snail:
#         break

# print(ans)
d = 0
r, c = 0, 0
for i in range(0, (T*T)):
    snail[r][c] = a[i]
    nr = r + dr[d]
    nc = c + dc[d]
    print(nr, nc)
    if 0 <= nr < T and 0 <= nc < T and snail[nr][nc] == 0: # snail[nr][nc]먼저 쓰면 nr, nc가 범위를 벗어나 index에러가 일어날 수 있음
        r, c = nr, nc
    else:
        d = d + 1 if d < 3 else 0
        r = r + dr[d]
        c = c + dc[d]
        print(r, c)
for i in snail:
    print(*i)
    # 다음 위치가 유효하지 않으면 방향 꺾기
    # nr, nc가 인덱스 범위안에 있어야 하고


T = int(input())

for tc in range(1, T+1):
    r = int(input())
    count = 0
    for i in range(1, 201):
        for j in range(1, 201):
            if i**2 + j**2 <= r**2:
                count += 1
    print(f'#{tc} {(count*4+4*r)+1}')
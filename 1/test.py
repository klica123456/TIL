def solution(park, routes):
    a = []
    b = []
    for i in park:
        a.append(list(i))
    for i in routes:
        b.append(list(i))
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    # df = [1, -1, 0, 0]
    # ds = [0, 0, 1, -1]
    j = 1
    r = 0
    c = 0
    answer = [0]*2
    for i in range(len(b)):
        if b[i][0] == 'E':
            # c = a[r][c+int(b[i][2])]
            if answer[1] + int(b[i][2]) < len(a):
                answer[1] += int(b[i][2])

            elif answer[1] + int(b[i][2]) >= len(a):
                answer[1] += 0

        elif b[i][0] == 'W':
            # c = a[r][c-int(b[i][2])]
            if answer[1] - int(b[i][2]) >= 0:
                answer[1] -= int(b[i][2])

            elif answer[1] - int(b[i][2]) < 0:
                answer[1] -= 0
                
        elif b[i][0] == 'S':
            # c = a[r+int(b[i][2])][c]
            if answer[0] + int(b[i][2]) < len(a):
                answer[0] += int(b[i][2])
        elif b[i][0] == 'N':
            # c = a[r-int(b[i][2])][c]
            if answer[0] - int(b[i][2]) >= 0:
                answer[0] -= int(b[i][2])
    print(answer)
    return answer









        
    
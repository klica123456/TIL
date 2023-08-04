import math
T = int(input())

for test_case in range(1, T+1):
    number, sc = map(int, input().split())
    op = number/10
    k = []
    n = []
    scores = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for j in range(number):
        a, b, c = map(int, input().split())
        k.append(0.35*a+0.45*b+0.2*c)
        n.append(0.35*a+0.45*b+0.2*c)
        k.sort(reverse = True)
        if j == sc-1:
            print(j)
            p = n[j]
            print(p)
            

    # for i in k:
    #     print(i)
    #     for j in range(number):
    #         dic = {}
    #         dic[i] = scores[math.trunc(j/op)]
            # if p == i:
            #     print(p)
            #     print(i)
            #     print(f"#{test_case} {dic[i]}")
            #     break
        # break









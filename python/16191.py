T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    num_dict = {}
    for i in num:
        if i not in num_dict.keys():
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    p = 0
    for i in num_dict.values():
        if i == max(num_dict.values()):
            p += 1
    if p == 1:
        max_num = max(num_dict, key=num_dict.get)
        print(f'#{tc} {max_num} {max(num_dict.values())}')
    if p > 1:
        lis = []
        for a, b in num_dict.items():
            if max(num_dict.values()) == b:
                lis.append(a)
                max_key = max(lis)
        print(f'#{tc} {max_key} {num_dict[max_key]}')

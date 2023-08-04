a = int(input())
k = []
for i in range(1,a+1):
    a = []
    a = list(str(i))
    i = 0
    for k in a:
        if '3' == k:
            i += 1
        elif '6' == k:
            i += 1
        elif '9' == k:
            i += 1
    if i > 0:
        print('-'*i, end = ' ')
    else:
        print(''.join(a), end = ' ')
    # for i in a:

    #     if i == '-':
    #         print('-', end = '')
    # if len(a) > 1:
    #     print(''.join(a), end = ' ')
    # else:
    #     print(*a, end = ' ')
        

    # if len(a) > 1:
    #     print(''.join(a), end = ' ')
    # else:
    #     print(*a, end = ' ')




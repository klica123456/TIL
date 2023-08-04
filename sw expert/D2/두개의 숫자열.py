T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    c, d = map(int, input().split())
    a = list(input().split())
    b = list(input().split())
    
    if len(a) > len(b):
        k = []
        for j in range((len(a)-len(b))+1):
            q = 0
            for i in range(len(b)):
                p = 0
                p = int(a[i+j])*int(b[i])
                # j += 1
                q += p
                # print(p)
                # print(q)
            k.append(q)
        print(f"#{test_case} {max(k)}")

    if len(a) < len(b):
        k = []
        for j in range((len(b)-len(a))+1):
            q = 0
            for i in range(len(a)):
                p = 0
                p = int(a[i])*int(b[i+j])
                q += p
            k.append(q)
        print(f"#{test_case} {max(k)}")
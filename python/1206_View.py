T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split())) # map을 안쓰면 input().split() 자체가 list가 되어 int로 형변환이 불가해서 에러뜸
    # 그래서 map으로 묶음
    # 밖의 반복문은 빌딩의 갯수를 세겠다.
    # 안의 반복문은 빌딩의 충수를 세는데 쓰겠다.
    # 조망권을 가지는 세대 수
    count = 0
    for i in range(2, N-2): # 양쪽 2칸씩은 무조건 높이가 0이므로 확인할 필요X
        height = buildings[i]
        for j in range(height, -1, -1): # 시작 = 꼭대기, 끝 = 0, 1씩 감소
            
            # 현재 i 번째 건물의 층수 j
            # j 층에서 양쪽 2칸을 확인한 다음 조망권이 있으면 count를 1씩 증가
            # 왼쪽 -1,-2 건물의 높이 확인, 오른쪽 +1, +2 건물의 높이 확인
            # 현재 j층이 왼쪽과 오른쪽 건물의 높이보다 높아야 조망권 ok
            # 왼쪽 - 1 => buildings[i-1]
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            else:
                break

    print(f'#{test_case} {count}')
    
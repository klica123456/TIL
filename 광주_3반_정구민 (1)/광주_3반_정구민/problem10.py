############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):
    # y = -1
    # for i in matrix:
    #     x = -1
    #     y += 1
    #     for j in i:
    #         x += 1
    #         if j == 1:
    #             return y,x
            
    row = 0
    col = 0
    for r in matrix:
        row += 1
    col = row
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 1:
                return (r,c)
    # 여기에 코드를 작성하여 함수를 완성합니다.
            


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    c = 0
    l = 0

    for i in matrix:
        c += 1
    row_list = [0]*c

    for i in matrix:
        k = 0
        e = 0
        for j in i:
            k += j
            e += 1
        row_list[l] += k
        l += 1
    
    col_list = [0]*e

    for i in matrix:
        b = 0
        for j in i:
            col_list[b] += j
            b += 1

    temp = 0
    temp1 = 0
    for i in row_list:
        if temp == 0 or i > temp:
            temp = i
    for i in col_list:
        if temp1 == 0 or i > temp1:
            temp1 = i
    if temp < temp1:
        return ('col', temp1)
    else:
        return('row', temp)


    row_len = 0 # 행 길이
    col_len = 0 # 열 길이

    # 행길이
    for r in matrix:
        row_len += 1
    # 열길이
    for c in matrix[0]:
        col_len += 1

    # 가로 합

    
    # 세로 합


    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
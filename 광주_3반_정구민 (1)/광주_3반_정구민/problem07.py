############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    l = 0
    for i in range(1, number):
        k = []
        if i == 17:
            continue
        for j in range(1, i+1):
            if i%j == 0:
                k.append(j)
        if len(k) == 2:
            l += j
    return l 

    # result = 0
    # for num in range(2, number):
    #     is_prime = True # 소수라고 가정후 시작
    #     if num == 17:
    #         continue
    #     for i in range(2, num):
    #         if num % i == 0:
    #             is_prime = False # num은 소수가 아니라고 체크
    #             break
    #     if is_prime: # is_prime이 처음 가정 그대로 소수인 경우만 함 구하기
    #         result += num
    # return result





    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
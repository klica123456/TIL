############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    # k = ''
    # for char in word:

    #     # 대문자인 경우
    #     if char.isupper():
    #         # char 가 'A'랑 얼만큼 떨어져 있는가??
    #         # ord(char) - 65
    #         # char 가 'C'라면 67, 'A'랑은 2만큼 떨어져 있다.
    #         # 그래서 내가 이 char를 얼만틈 밀었는데? => num
    #         # 29번 미는거랑 3번 미는거랑 똑같다. num%26
    #         # (ord(char) - 65 + num) % 26 => 'A'랑 얼만큼 떨어져 있는지 구함
    #         # 다시 문자로 바꾸면 되는데 chr()
    #         temp = chr((ord(char) - 65 + num) % 26 + 65)
    #     # 소문자인 경우
    #     elif char.islower():
    #         temp = chr((ord(char) - 97 + num) % 26 + 97)
    #     k += temp
    # return k

    l = []
    a = {}
    k = 0

    for i in word:
        k += 0
        l.append(ord(i)+num)
        if i.islower() == True:
            a[k] = True
        else:
            a[k] = False
        k += 1

    for i, k in a.items():
        if k == True:
            while l[i] > 122:
                l[i] -= 26
        if k == False:
            while l[i] > 90:
                l[i] -= 26
    c = ''

    for i in l:
        c += chr(i)
    return c
    

    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.

    
def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        if i+1 == len(arr)-1:
            answer.append(arr[i+1])
    return answer

arr = [4, 4, 4, 3, 3]
print(solution(arr))
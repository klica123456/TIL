# from math import ceil
#
# def solution(progresses, speeds):
#     answer = []
#     max_cnt = 0
#     cnt = 0
#     for i in range(len(progresses)):
#         k = ceil((100 - progresses[i]) / speeds[i])
#         if max_cnt < k:
#             max_cnt = k
#             answer.append(cnt)
#             cnt = 1
#         else:
#             cnt += 1
#
#     return answer[1:] + [cnt]

def solution(progresses, speeds):
    l = []
    answer = []
    for i in range(len(progresses)):
        k = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            k += 1
        l.append(k)
    q = 0
    cd = 0
    for i in range(len(l)):
        if cd < l[i]:
            cd = l[i]
            answer.append(q)
            q = 1
        else:
            q += 1
        # if i == len(l)-1:
        #     answer.append(q)
    return answer[1:] + [q]


p = [90, 90, 90, 90]
s = [5, 3, 4, 1]

print(solution(p, s))



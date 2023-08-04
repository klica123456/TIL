A = [0, 1, 5, 4, 6, 4, 2]
k = 6
B = [0] * len(A)

def Counting_Sort(A, B, k):
    C = [0] * (k+1)
    for i in range(0, len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B
#
# A = [0, 1, 5, 4, 6, 4, 2]
# k = 6
# B = []
print(Counting_Sort(A, B, k))

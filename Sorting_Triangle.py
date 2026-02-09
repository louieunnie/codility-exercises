# Right Answer: Time Complexity O(N*log(N))
def solution(A):
    A.sort() # O(N*log(N))

    N = len(A)
    for i in range(N-2): # O(N)
        if A[i] + A[i+1] > A[i+2]:
            if A[i] + A[i+2] > A[i+1]:
                if A[i+2] + A[i+1] > A[i]:
                    return 1
    return 0
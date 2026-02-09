# Right answer:  Time Complexity O(N * log(N))
def solution(A):

    A.sort() # O(N * log(N))

    if A[-1] > 0 and A[-2] > 0 and A[-3] > 0:
        big = A[-1] * A[-2] * A[-3]
        if A[0] < 0 and A[1] < 0:
            b = A[-1] * A[0] * A[1]
            if big < b:
                big = b
        return big
    elif A[-1] > 0 and A[-3] <= 0:
        return A[-1] * A[0] * A[1]
    elif A[-1] <= 0:
        return A[-1] * A[-2] * A[-3]
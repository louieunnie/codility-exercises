def solution(A, B, K):
    # Time Complexity O(N)
    # cnt = 0
    # for n in range(A, B+1):
    #     if n % K == 0:
    #         cnt += 1
    # return cnt
    
    # Time Complexity O(1)
    first = 0
    exist = False
    for n in range(A, B+1):
        if n % K == 0:
            exist = True
            first = n
            break
    if not exist: # when there is no first (not equal to first ==0)
        return 0 
    rem = (B-first) // K
    return rem + 1
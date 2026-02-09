# wrong answer: Time Out Error (Time Complexity O(n^2))
def solution(A):
    cnt = 0 
    for i in range(len(A)): 
        if A[i] == 0: 
            for j in range(i+1, len(A)): 
                if A[j] == 1: 
                    cnt += len(A)- (j+1) 
    return cnt

# right answer: adding prefix (in this case the number of zeros) in advance => Time Complexity O(n)

def solution(A):
    zeros = 0
    pairs = 0
    for i in range(len(A)):
        if pairs > 1000000000:
            return -1
        if A[i] == 0:
            zeros += 1
        elif A[i] == 1:
            pairs += zeros
        
    return pairs
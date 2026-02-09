# Wrong Answer: Time Out Error => Time Complexity O(N^2)
def solution(A):
    # 교차: 두 원의 중심 간 거리가 두 원의 반지름의 합보다 작음
    
    cnt = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if j-i <= A[i] + A[j]:
                cnt += 1
                # print((i, j))
    return cnt
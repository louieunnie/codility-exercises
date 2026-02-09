# Right answer: use the cummulative number of each letters!
def solution(S, P, Q):
    # Step 1
    # prefix 배열 (index 별 각 character 누적 등장 횟수) 만들기
    # i번째 index => 0..i-1까지의 누적 갯수를 나타냄
    N = len(S)

    cum_A = [0] * (N+1)
    cum_C = [0] * (N+1)
    cum_G = [0] * (N+1)
    cum_T = [0] * (N+1)

    for i in range(N): # Time Complexity O(N)
        cum_A[i+1] = cum_A[i]
        cum_C[i+1] = cum_C[i]
        cum_G[i+1] = cum_G[i]
        cum_T[i+1] = cum_T[i]

        if S[i] == "A":
            cum_A[i+1] += 1
        elif S[i] == "C":
            cum_C[i+1] += 1
        elif S[i] == "G":
            cum_G[i+1] += 1
        elif S[i] == "T":
            cum_T[i+1] += 1

    # Step 2
    # 쿼리 별로 존재하는 알파벳 확인
    res = []
    for i in range(len(P)): # Time Complexity O(M) (<-number of queries)
        curr = []
        start = P[i]
        end = Q[i]+1
        if cum_A[end]-cum_A[start] > 0:
            curr.append(1)
        if cum_C[end]-cum_C[start] > 0:
            curr.append(2)
        if cum_G[end]-cum_G[start] > 0:
            curr.append(3)
        if cum_T[end]-cum_T[start] > 0:
            curr.append(4)
        res.append(min(curr))
    return res


# Wrong answer: Time out error & Too complex
def solution(S, P, Q):
    impact_factors = {}
    for i in range(len(S)): # O(S)
        if S[i] == "A":
            impact_factors[i] = 1
        elif S[i] == "C":
            impact_factors[i] = 2
        elif S[i] == "G":
            impact_factors[i] = 3
        elif S[i] == "T":
            impact_factors[i] = 4
    curr = []
    res = []
    for j in range(P[0], Q[0]+1):
        curr.append(impact_factors[j])
    res.append(min(curr))
    
    for i in range(1, len(P)):
        if P[i] > Q[i-1] or Q[i] < P[i-1]:
            curr = []
            for j in range(P[i], Q[i]+1):
                curr.append(impact_factors[j])
            res.append(min(curr))
            continue
        if P[i] > P[i-1]:
            for k in range(P[i-1], P[i]):
                curr.pop(0)
        elif P[i] < P[i-1]:
            for k in range(P[i-1]-1, P[i]-1, -1):
                curr.insert(0, impact_factors[k])
        if Q[i] > Q[i-1]:
            for k in range(Q[i-1]+1, Q[i]+1):
                curr.append(impact_factors[k])
        elif Q[i] < Q[i-1]:
            for k in range(Q[i], Q[i-1]):
                curr.pop()
        res.append(min(curr))
    return res
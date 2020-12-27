
N, K = map(int, input().split(' '))
cnt = 0
nums = [False] * (N+1)

for i in range(2, N+1):
    if nums[i]:
        continue

    for j in range(i, N+1, i):
        if nums[j]:
            continue
        cnt += 1
        nums[j] = True
        
        if cnt == K:
            print(j)
            break
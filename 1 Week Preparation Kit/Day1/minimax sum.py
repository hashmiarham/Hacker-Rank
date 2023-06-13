def minimaxsum(arr):
    max_sum = 0
    min_sum = float('inf')
    narr = []
    s = 0
    for i in range(5):
        s = 0  # Reset the sum for each iteration of i
        for j in range(5):
            if j != i:
                s += arr[j]
        narr.append(s)
        if s > max_sum:
            max_sum = s
        if s < min_sum:
            min_sum = s
    
    print( min_sum,max_sum)


y = input()
arr = list(map(int, y.split()))
minimaxsum(arr)

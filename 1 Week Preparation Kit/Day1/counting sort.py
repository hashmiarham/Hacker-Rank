def counting_sort(arr):
    counts = [0] * 100
    
    for num in arr:
        counts[num] += 1
    
    return counts

n = int(input())
arr = list(map(int, input().split()))

result = counting_sort(arr)

print(*result)
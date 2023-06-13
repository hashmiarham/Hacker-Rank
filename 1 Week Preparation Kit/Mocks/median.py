def find_median(arr):
  sorted_arr = sorted(arr)
  n = len(sorted_arr)
  middle_index = n // 2

  return sorted_arr[middle_index]


n = int(input())
y = input()
arr = list(map(int, y.split()))
median = find_median(arr)
print(median)

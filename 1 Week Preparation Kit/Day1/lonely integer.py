#USING CONVENTIONAL METHOD
def lonelyint(arr, n):
    cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1
                
        if cnt > 1:
            continue
        else:
            print(arr[i])

n = int(input())
y = input()
arr = y.split()
lonelyint(arr, n)



#LONELY INTEGER USING XOR

# def lonelyint(arr, n):
#     cnt = 0
#     for i in range(n):
#         cnt = cnt^int(arr[i])
#     return cnt


# n = int(input())
# y = input()
# arr = y.split()
# x = lonelyint(arr, n)
# print(x)

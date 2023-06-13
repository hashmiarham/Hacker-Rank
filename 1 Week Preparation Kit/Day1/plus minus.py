def plusminus(arr):
    rn=0
    rz=0
    rp=0
    cn=0
    cz=0
    cp=0
    for i in range(len(arr)):
        if(int(arr[i])<0):
            cn+=1
            rn=cn/(len(arr))
        elif(int(arr[i])==0):
            cz+=1
            rz=cz/(len(arr))
        elif(int(arr[i])>0):
            cp+=1
            rp=cp/(len(arr))
    print(rp)
    print(rn)
    print(rz)



n=int(input())
y=(input())
arr=y.split()

plusminus(arr)
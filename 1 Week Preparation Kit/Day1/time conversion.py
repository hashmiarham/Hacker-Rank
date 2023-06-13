def tformatchg(t):
    l=len(t)
    if(t[-2:]=="AM" or t[-2:]=="am"):
        h=int(t[:2])
        if(h!=12):
            print(t[:-2])
        else:
            ht="00"
            print(ht+t[2:-2],end="")
    else:
        h=int(t[:2])
        if(h!=12):
            hf=h+12
            print(str(hf)+t[2:-2],end="")
        else:
            ht="12"
            print(ht+t[2:-2],end="")
        
t=input()
tformatchg(t)
a = int(input("Enter the amount"))
b = a - 100
c = b // 2000
if 0 > c < 1 :
    d = b//500
else:
        d = (b%2000)//500
if 0 < d <  1 :
    e = b//100
else:
        e = ((b%2000)%500)//100
        f = e + 1
        print(f" The number of 2000 notes is {c} \nThe number of 500 notes is {d} \nThe number of 100 notes is {f}") 


n=int(input("enter the number"))
s=n*n
k=str(s)
l=int(k[-1])
if l==n:
    print("it is an automorphic ")
else:
    print("it is not an automorphic number")
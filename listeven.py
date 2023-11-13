n=input("entre list of numbers")
l=list(map(int,n.split(",")))
t=[ i for i in l if(i%2==0)]
print(t)

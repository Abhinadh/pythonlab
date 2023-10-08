s=input("enter numbers ")
n=list(map(int,s.split(",")))
even=[i for i in n if(i%2==0)]
print(even)

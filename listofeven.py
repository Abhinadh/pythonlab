n=input("enter the list of number")
s=list(map(int,n.split(",")))
even=[i for i in s if(i%2==0) ]
print("even numbers",even)

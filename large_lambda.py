"""large of two using lambda"""
large=lambda a,b:a if a>b else b
n=input("enter  two value")
a,b=list(map(int,n.split(",")))
print(large(a,b))

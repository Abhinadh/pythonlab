def number(n):
    for i in n:
        if i==237:
            break
        elif  not (i%2):
            print(i)
n=input("entre some numbers sepetrated with comma")
s=list(map(int,n.split(',')))
number(s)

        

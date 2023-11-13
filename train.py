class train:
    def __init__(self):
        self.trainname=input("enter the train name")
        self.noofseats=int(input("enter number of seats"))
    def display(self):
        print ("trainname=",self.trainname)
        print("no of seats balance=",self.noofseats)
    def reserve(self):
        n=int(input("enter reserved seats"))
        if (n>self.noofseats):
            return " seats not enough"
        else:
            self.noofseats=self.noofseats-n
            return self.noofseats
            
    def cancel(self):
        n=int(input("enter cancelled seats"))
        self.noofseats=self.noofseats+n
        return self.noofseats
try:
    a=train()
    print(a.reserve())
    print(a.display())
    print(a.cancel())
except exception as e:
    print(e)

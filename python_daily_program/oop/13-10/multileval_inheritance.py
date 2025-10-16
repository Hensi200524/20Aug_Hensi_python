
class Hensi:
    hid:int
    htech:str
    
    def h_getdata(self):
        self.hid=input("Enter Hensi's ID:")
        self.htech=input("Enter Hensi's Tech:")
        
class Bhargav(Hensi):
    bid:int
    btech:str
    
    def b_getdata(self):
        self.bid=input("Enter Bhargav's ID:")
        self.btech=input("Enter Bhargav's Tech:")

class Krisha(Bhargav):
    kid:int
    ktech:str
    
    def k_getdata(self):
        self.kid=input("Enter Krisha's ID:")
        self.ktech=input("Enter Krisha's Tech:")

class tops(Krisha):
    def printdata(self):
        print("------Hensi's Data------")
        print("Hensi's ID:",self.hid)
        print("Hensi's Tech.:",self.htech)
        print("------Bhargav's Data------")
        print("Bhargav's ID:",self.bid)
        print("Bhargav's Tech.:",self.btech)
        print("------Krisha's Data------")
        print("Krisha's ID:",self.kid)
        print("Krisha's Tech.:",self.ktech)
    
tp=tops()
tp.h_getdata()
tp.b_getdata()
tp.k_getdata()
tp.printdata()

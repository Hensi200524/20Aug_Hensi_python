
class ashok:
    aid:int
    atech:str
    
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Tech:")
        
class sanket:
    sid:int
    stech:str
    
    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.stech=input("Enter Sanket's Tech:")

class nirav:
    nid:int
    ntech:str
    
    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.ntech=input("Enter Nirav's Tech:")

class tops(ashok,sanket,nirav):
    def printdata(self):
        print("------Ashok's Data------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Tech.:",self.atech)
        print("------Sanket's Data------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Tech.:",self.stech)
        print("------Nirav's Data------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Tech.:",self.ntech)
    
tp=tops()
tp.a_getdata()
tp.s_getdata()
tp.n_getdata()
tp.printdata()

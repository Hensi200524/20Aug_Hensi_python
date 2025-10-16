
class acopen:
    mainbal=0
    acno:int
    acnm:str
    actype:str
    def account(self):
        self.acno=input("Enter your A/c No:")
        self.acnm=input("Enter Your A/c Name:")
        self.actype=input("Enter your A/c Type:")
    
class deposite(acopen):
    def depo(self):
       self.am=int(input("Enter your deposite amount:"))
       if self.am>=2000:
           self.mainbal+=self.am
           print("Balance:",self.mainbal)
       else:
           print("Error!Plz enter min. Rs.20000/-")

class withdrwal(deposite):
    def withdr(self):
        self.am=int(input("Enter your withdrwal amount:"))
        if self.am>self.mainbal:
            print("Error!Insufficient Balance")
        else:
            self.mainbal-=self.am
            print("Current Balance:",self.mainbal)
        
class statements(withdrwal):
    def print_statement(self):
        print("A/c No:",self.acno)
        print("A/c Name:",self.acnm)
        print("A/c Type:",self.actype)
        print("Main Balance:",self.mainbal)
        
        
st=statements()
st.account()
st.depo()
st.withdr()
st.print_statement()

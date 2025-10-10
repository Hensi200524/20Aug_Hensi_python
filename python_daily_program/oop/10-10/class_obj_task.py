class student_data:
    # id:int
    # name:str
    def getdata(self):
        self.id = int(input("Enter Id: "))
        self.name = input("Enter Name: ")

    def showdata(self):
        print("Id:", self.id)
        print("Name:", self.name)   

std= student_data()
std.getdata()
std.showdata()
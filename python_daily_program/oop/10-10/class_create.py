class student_info:
    stid = 101
    stnm = "Hensi"

    def showmsj(self): 
        print("This is message function")

si=student_info()
print("Id:",si.stid)
print("name:",si.stnm)
si.showmsj()


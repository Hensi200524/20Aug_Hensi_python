def studdata(id,name,sub):
    print("id:",id)
    print("name:",name)
    print("sub:",sub)

#getdata(101,"hensi","python")

n = int(input("enter number of students:"))
for i in range(n):
    sid= int(input("enter id:"))
    sname= input("enter name:")
    ssub= input("enter sub:")

    #function call
    studdata(sid,sname,ssub)


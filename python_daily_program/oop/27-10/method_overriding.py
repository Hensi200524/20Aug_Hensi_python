class master:
    #method overriding
    def header(self,p_name):
        print(f"welcome to {p_name}.")

class home(master): #refrencing master class
    def header(self, p_name):
        return super().header(p_name)

class contact(master): #refrencing master class
    def header(self, p_name):
        return super().header(p_name)

h1 = home()
h1.header("Home Page")

c1 = contact()
c1.header("Contact Page")
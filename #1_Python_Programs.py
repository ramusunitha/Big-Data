class cls1:
    class_attrib=100 #class attribute or member variable
    def funct1(self,a,b):
        return a+b+self.class_attrib
    def funct2(self, a, b):
        return a+b-self.class_attrib

print("Sairam")
obj1=cls1()
x=obj1.funct1(100,200)
y=obj1.funct2(300,400)
print(x,y)

Output:

/home/hduser/PycharmProjects/pythonProject/venv/bin/python /home/hduser/PycharmProjects/WE39Project/PkgPythonProg/PkgPythonDev/ModShowroom.py
Sairam
400 600

Process finished with exit code 0

#class student:
 #   def SayHello(self):
  #      print("Hello")

#Abebe=student()
#Redwane=student()
#Redwane.SayHello()

#print(id(Abebe))
#print(id(Redwane))

#class student:
 #   def SayHello(self):
  #      print("Hello")
"""
#s1=student()
#s2=student()
#s1.SayHello()
#s2.SayHello()
"""
#class student:
    def SayHello(self):
        print("Hello" + self.FName)
#s1=student
#s2=student
#s1.FName="Redwane"


class student:
    def __init__(self,fn,ln):
        self.FName= fn
        self.LName= ln
    def SayHello(self):
        print("Hello" +self.FName + " " + self.LName)

 s1=student("Abebe","Ayele")
 s1.SayHello() 
 s2=student("Yoseph","Kassaye") 
 s2.SayHello() 


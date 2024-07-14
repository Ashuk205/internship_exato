# def hello( ):
#    print( "hello")


# hello()
# sales1 =6000
# profit1 = 2000
# ad1 = 1000

# sales2= 6000
# profit2 = 2000
# ad2 = 1000

# sales3 = 6000
# profit3 = 2000
# ad3 = 1000 

class person:
     name = "Ashutosh"
     occupation = "software devloper"
     networth = 10 
     def info(self):
          print(f"{self.name} is a {self.occupation}")



a = person()
b = person()
a.name = "Ashutosh " 
a.occupation = "Accountant"
# print(a.name, a.occupation)

b.name =  "Ritika"
b.occupation = "IAS offcier"
a.info()
b.info()
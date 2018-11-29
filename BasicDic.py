import math as m
import DicLibrary as DicL

emp = {}
emp = {"Name":"Somsak","Age":25,"Height":170,"Address":"Pattanakarn"}

#print(emp)
emp["Gender"] = 'M'

#print(emp)

if "name" is emp.keys():
    print("No")
#del emp["Name"] = delete

emp["Weight"] = 55
emp["BMI"] = '{0:.2f}'.format(emp["Weight"]/m.pow(emp["Height"]/100,2))

#print(emp)
#Check key
#print(emp.keys())

DicL.line40()
for i in emp.keys():
    print(i)
DicL.line40()
for i in emp.values():
    print(i)
DicL.line40()
for i in emp.items():
    print(i)

import DicLibrary as DicL
import os.path


numberProduct = int(input("Enter Number of New Product : "))

productlist = []
for i in range(numberProduct):
    print("\nProduct Number [{0}]".format(i+1))
    DicL.lineQ()
    name = input("Enter product name : ")
    price = input("Enter product price : ")
    stock = input("Enter product stock : ")
    productlist += [[name , price , stock]]

def workingWithFile(filename,text,m):
    #CONTECT MANAGER WITH
    with open(filename,mode=m) as f:
        f.write(text)


if __name__ == '__main__':
    File = "myFile/products.csv"
    if os.path.exists(File):
        workingWithFile(File,productlist,"a")
        encoding = "UTF-8"
    else:
        workingWithFile(File,productlist,"x")
        encoding = "UTF-8"
        print("Success Write File")


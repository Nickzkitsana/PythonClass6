#Slide 226
import os.path

def workingWithFile1(filename,m):
    f = open(filename,mode=m)
    f.write("Kitsana\nTest\n")
    f.close()

def workingWithFile2(filename,m):
    #CONTECT MANAGER WITH
    with open(filename,mode=m) as f:
        f.write("{:.2f}".format(123.2575))


if __name__ == '__main__':
    workingFile = "myFile/Student3.txt"
    mode = "x"
    if os.path.exists(workingFile):
        print("File Exist")
    else:
        workingWithFile2(workingFile,mode)
        print("Success Write File")

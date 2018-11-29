def readFile1(filename): #.read()
    with open(filename,"r",encoding="UTF-8")as f:
        data = f.read()
        print(data)

def readFile2(filename): #.readline()
    with open(filename,"r",encoding="UTF-8")as f:
        data = f.readline()
        #print(data,end="") #ปริ้นแล้วไม่ขึ้นบรรทัดใหม่
        #data = f.readline()
        #print(data,end="")
        for i in f: #Readline() --> \n
            print(i,end="")

def readFile3(filename): #.readlines()
    with open(filename,"r",encoding="UTF-8")as f:
        num =1
        for i in f:
            datasplit = i.split('\n')
            print("{0}.) {1}".format(num,datasplit[0]))
            num +=1

if __name__ == '__main__':
    filename = "myFile/MarvelComics.txt"
    readFile3(filename)

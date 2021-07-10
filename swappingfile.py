def swapfileData():
    filename1=input("Enter the file name: ")
    filename2=input("Enter the file name to be swapped: ")
    
    with open(filename1,'r') as a:
        data_a = a.read
    with open(filename2,'r') as b:
        data_b = b.read
    with open(filename1,'w') as a:
        data_b = a.write(filename2)
    with open(filename2,'w') as b:
        data_a = b.write(filename1)
    

swapfileData()
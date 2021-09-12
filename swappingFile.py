
def swapFileData():
    file1Input=input("enter name of file 1")
    file2Input=input("enter name of file 2")
    with open(file1Input, 'r') as a:
       data_a=a.read 
   
    with open(file2Input, 'r') as b:
        data_b=b.read
    
    with open(file1Input, 'w') as a:
        a.write(data_b)

    with open(file2Input, 'w') as b:
        b.write(data_a)
    
swapFileData()
    
    
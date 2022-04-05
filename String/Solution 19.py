
def prin(l1,l2):
    for i in range(3):
        print('{} live in {}'.format(l1[i],l2[i]))
def inpu():
    l1=[]
    l2=[]
    for i in range(3):
        l=input("Enter the name of student's : ")
        l1.append(l)
        l=input("Enter the Address of student's : ")
        l2.append(l)
    prin(l1,l2)
inpu()

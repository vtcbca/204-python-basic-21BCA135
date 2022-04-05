
x=[]
a=0
for i in range (5):
    s=input('Enter any string : ')
    x.append(s)
print(x)
for i in x:
    if len(i)%2==0:
        a=a+1
print('\nTotal sring of even number of character is ',a,'\n')
for i in x:
    if len(i)%2==0:
        print(i)

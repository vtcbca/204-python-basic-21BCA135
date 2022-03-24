a=input("Enter any string : ")
l=list(a.split ())
c=0
for i in l:
    b=l[c][::-1]
    if l[c]==b:
        c=c+1
        print (l[c])
print("Total {} palindrom word in string {}".format(c,l[c]))


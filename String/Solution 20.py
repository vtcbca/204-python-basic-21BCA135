
def palin():
    s=input('Enter any string : ')
    r= "".join(reversed(s))
    if s==r:
        print("{} is palindrom".format(s))
    else :
        print ("{} is not palindrom.".format(s))
palin()

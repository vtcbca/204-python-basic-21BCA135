
def strSymmetric(s):
    b=s
    a=len(s)//2
    if s[:a]==s[a:]:
        print(b,' is a symmetric string.')
    else:
        print(b,' is not a symmetric string.') 
def inpu():
    s=input('Enter any string : ')
    strSymmetric(s)
inpu()

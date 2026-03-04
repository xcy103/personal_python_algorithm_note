

def exgcd(a,b):
    if b==0:
        return a,1,0
    d,x1,y1 = exgcd(b,a%b)
    x = y1 
    y = x1 - (a//b)*y1
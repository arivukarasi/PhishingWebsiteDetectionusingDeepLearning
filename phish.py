def URLhavingattherate(URL): #4th column
    if '@' in URL:
        return 0
    else:
        return 1
def Redirectusingdoubleslash(URL):#5th column
    p=0
    for i in range(len(URL)-1):
        if URL[i]=="/" and URL[i+1]=="/":
            p=i
    if p>7:
        return 0
    else:
        return 1
def prefixsuffix(URL): #6th column
    if '-' in URL:
         return 0
    else:
        return 1
def Length(URL): #2nd column
    if len(URL)<54:
         return 1
    else:
        return 0.
def TinyURL(URL): #3rd column
    if 'bit.ly' in url:
         return 1
    else:
        return 0
def IP(URL):#1st Column
    if URL.count('x')>6:
        return 0
    else:
        return 1
def Dot(URL):#7th column
    if URL.count('.')>3:
        return 0
    else:
        return 1
def HTTPS(URL):#8th column
    if 'https' in URL:
        return 1
    else:
        return 0
def valid(e):
    if e<=1:
        return 1
    else:
        return 0
def favicon(f):
    if f==1:
        return 1
    else:
        return 0
url = input()
exp = int(input())
L=[]
for i in range(30):
    L+=[0]
c9 = valid(exp)
L[8] = c9
c8 = Dot(url)
L[7] = c8
c7 = Dot(url)
L[6] = c7
c1 = IP(url)
L[0] = c1
c3 = TinyURL(url)
L[2]=c3
c2 = Length(url)
L[1] = c2
p = URLhavingattherate(url)
L[3]=p
k = Redirectusingdoubleslash(url)
L[4]=k
s = prefixsuffix(url)
L[5]=s
f = int(input())
c10 = favicon(f)
L[9] = c10
print(*L)

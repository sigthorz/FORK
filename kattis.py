#skilaverkefni1
#a
bergmal_output = input()

if len(bergmal_output) > 1000 or len(bergmal_output) < 1:
    print("villa")

else:
    print(bergmal_output)

#b
hiti_daga = []
dagar = int(input())
hiti_daga=list(map(int,input().split()))

print(max(hiti_daga))
print(min(hiti_daga))

#c
h1,h2=map(int,input().split())
p1,p2=map(int,input().split())
if h1!=p1 and h2!=p2:
    print(2)
else:
    print(1)
#skilaverkefni2
#d
n,m=map(int,input().split())
lina=[]
linur=[]
fjoldi=0
for i in range(n):
    lina=list(input())
    fjoldi+=lina.count('*')
    linur.append(lina)
print(fjoldi)
for x in range(n):
    for y in range(m):
        if linur[x][y]=='*':
            print(x+1,y+1)
#e
n=int(input())
for i in range(n):
    lina=input().lower()
    print(lina.capitalize())
#f
dicta={}
for j in range(1,j+1):
    dicta[j]=0
print(dicta)
for i in range(i): 
    a,b=map(int,input().split())
    dicta[b]=dicta[b]+1
print(min(dicta.values()))
#g
listi=input().split(';')
#print(listi)
listiint=[]
for x in listi:
    #print(x)
    if '-' in x:
        temp=list(map(int,(x.split("-"))))
        for i in range(temp[0],temp[1]+1):
            listiint.append(i)
    else:
        listiint.append(int(x))
print(len(listiint))
#skilaverkefni 3
#i
dagatal={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
man=int(input())
print(dagatal[man])
#j
n,k=map(int,input().split())
listi=list(map(int,input().split()))
x=listi.index(k)
if x==0:
    print("fyrst")
elif x==1:
    print("naestfyrst")
else:
    print(x+1,"fyrst")
#l
n,m,k=map(int,input().split())
bord=[]
temp=[]
for i in range(n):
    for j in range(m):
        temp.append('.')
    bord.append(temp)
    temp=[]
for x in range(k):
    x,y=map(int,input().split())
    bord[x-1][y-1]='*'
for lina in bord:
    print("".join(lina))

#m
n,r,c=map(int,input().split())
listi=[]
temp=[]
for i in range(r):
    listi.append(input().split())
bekkur=[]
temp1=[]
x=0
for i in range(n):
    temp1.append(input())
    x+=1
    if  x >= c:
        bekkur.append(temp1)
        temp1=[]
        x=0
y=0
for x in listi:
    if x[0] ==bekkur[y][0]:
        print("left")
    else:
        print("right")
    y+=1
#n
n=int(input())
listi=list(map(int,input().split()))

rod={}
for i in range(n):
    rod[listi[i]]=i
svar=[]
for x in sorted(rod.keys()):
    svar.append(str(rod[x]+1))
svar.reverse()
print(" ".join(svar))

#skilaverkefni4
#a
n = int(input())
k = str(input())
ord = str(input())

if k in ord:
    print("Unnar fann hana!")
else:
    print("Unnar fann hana ekki!")
#B
n = int(input())
for x in range(n):
    print(x + 1)
#C
mork = int(input())
lidSkora = int(input())

if mork == 2 and lidSkora == 2:
    print("Jebb")
elif mork == 0:
    print("Jebb")
else:
    print("Neibb")
#D
a, b, c = map(int, input().split())

if (a**2) + (b**2) == c**2:
    print((a*b) // 2)
elif (b**2) + (c**2) == a**2:
    print((c*b) // 2)
elif (a**2) + (c**2) == b**2:
    print((c*a) // 2)
else:
    print(-1)
#E
n = int(input())
numer = list(map(int, input().split()))

numer.sort()
listi = []

i = n / 3

listi.append(numer[int(i): int(2*i)])
listi.append(numer[0: int(i)])
listi.append(numer[int(-i):])

for x in listi:
    print(*x, end=" ")

print()
#F
n, m = map(int,input().split())

if n%(m+1) != 0:
    print("Jebb")
else:
    print("Neibb")
#G
keystrokes = str(input())

i = 0
passwd = []


for x in keystrokes:
    if x == "L":
        if i > 0:
            i -= 1
    elif x == "R":
        if i < len(passwd):
            i += 1
    elif x == "B":
        if len(passwd) != 0:
            i -= 1
            passwd.pop(i)
    else:
        passwd.insert(i, x)
        i += 1

for w in passwd:
    print(w, end="")

print()
#I
Trump = int(input())
Kim = int(input())


if Trump > Kim:
    print("MAGA!")
elif Trump < Kim:
    print("FAKE NEWS!")
else:
    print("WORLD WAR 3!")
#J
n = int(input())
listi = []
for q in range(n):
    listi.append(int(input()))

print(min(listi))
#K
fjoldiSpurninga, fjoldiNemenda = map(int, input().split())
svarLykill = list(map(str, input().split()))
listi = []


for q in range(fjoldiNemenda):
    nafn = str(input())
    svor = list(map(str, input().split()))
    svorRett = 0
    for w in range(len(svarLykill)):
        if svarLykill[w] == svor[w]:
            svorRett += 1
    prosenta = svorRett / fjoldiSpurninga
    einkun = round(prosenta*20) / 2
    bruh = []
    bruh.append(nafn)
    bruh.append(einkun)
    listi.append(bruh)

for x in listi:
    print(x[0] + ":", x[1])
#L
n = int(input())
stadsetningar = []
for q in range(n):
    coordinates = list(map(int, input().split()))
    stadsetningar.append(coordinates)
m = int(input())
sendar = []
for q in range(m):
    sendar.append(int(input()))
for q in sendar:
    mottakendur = 0
    for w in stadsetningar:
        if ((w[0] > -1 and q > w[0]) or (w[0] < 0 and q < w[0])) and ((w[1] > -1 and q > w[1]) or (w[1] < 0 and q < w[1])):
            mottakendur += 1

    print(mottakendur)
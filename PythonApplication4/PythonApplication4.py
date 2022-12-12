from random import randint
import random


a=int(float(input("Choose your lvl of difficulties: Tase1-1, Tase2-2, Tase3-3?")))
list=['+','-','//']
list2=['*','**','-']
list3=['//','*','+']
c=0
b=0
for i in range(5):
    r = randint(13,35)
    b = randint(0,30)
    g = random.choice(list)
    h = random.choice(list2)
    k = random.choice(list3)
    if a==1:
        print(f"{r}{g}{b}")
        p=int(float(input("")))
    if a==2:
        print(f"{r}{h}{b}{h}{r}")
        p=int(float(input("")))
    if a==3:
        print(f"{r}{k}{b}{k}{r}{k}{b}")
        p=int(float(input("")))
    if p==r+b or p==r-b or p==r//b or p==r*b**r or p==r**b-r or p==r-b*r or p==r*b-r or p==r**b*r or p==r-b**r or p==r-b-r or p==r*b*r or p==r**b**r or p==r//b*r+b or p==r//b+r*b or p==r*b+r//b or p==r*b//r+b or p==r+b*r//b or p==r+b//r*b or p==r//b/r//b or p==r*b*r*b or p== r+b+r+b or p==r//b*r*b or p==r//b+r+b or p==r+b//r//b or p==r+b*r*b or p==r*b+r+b or p==r*b//r//b:
     print("very well")
     c+=1
    else:
         print("wrong")
b+=1
v=round(c/b*100, 2)
print(f"Tulemus:{v}")
if v<=59:
    hinne="Teie hinne on 2"
elif p>=60 and p<=74:
    hinne="Teie hinne on 3"
elif p>=75 and p<=89:
    hinne="Teie hinne on 4"
else:
    hinne="Teie hinne on 5"
print(hinne)

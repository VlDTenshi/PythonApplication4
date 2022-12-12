nimi=input("Mis on sinu nimi?:")
tahed=list(nimi)
n=len(tahed)
print(f"{n} tahed: {tahed}")
print("Remove kasutamine")
t=input("Sisesta taht, mis vaja kustutada ara:")
nt=tahed.count(t)
print(nt)
j=0
if nt==0:
    print(f"{t} ei ole listis")
else:
    #for i in range(nt):
    #    if tahed [i-j]==t:
    #        tahed.remove(tahed[i-j])
    #        j+=1
    for i in range(len(tahed)):
        if tahed [i-j]==t:
            tahed.pop(i-j)
            j+=1
    print(f"Nuud {t} ei ole listis, on jaanud {tahed}")
t=input("Mis taht vaja otsida? ")
print(f"{t} seisab {tahed.index(t)+1} positsioonil")
maad=["Tallinn","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Lääne-Virumaa","Jõgevamaa","Tartu linn","Tartumaa","Põlvamaa","Võrumaa","Valgamaa","Viljandimaa","Järvamaa","Harjumaa","Raplamaa","Pärnumaa","Läänemaa","Hiiumaa","Saaremaa"]

index=""
n=0
while type(index)!=int or n!=5:
    try:
        index=int(input("Index:"))
        n=len(str(index))
    except:
        print("Vale index!")
index_list=list(str(index))
print(maad[int(index_list[0])-1])

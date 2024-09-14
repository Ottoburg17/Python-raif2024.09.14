import beolvas


szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

# műveletek
osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1/szam2
maradek =  szam1/szam2
hatvany = szam1**szam2
hatvany2 = szam1**szam2

# kiírás

print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1)+"-"+str(szam2)+"="+str(kulonbseg))
print(str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print(str(szam1)+"/"+str(szam2)+"="+str(hanyados))
print(str(szam1)+"%"+str(szam2)+"="+str(maradek))
print(str(szam1)+"^"+str(szam2)+"="+str(hatvany))
print(str(szam2)+"^"+str(szam1)+"="+str(hatvany2))
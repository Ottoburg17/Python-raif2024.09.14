# 1, a feladat
egeszSzam = 8
# 1,a feadat ellenőrzése
print(egeszSzam)
print(type(egeszSzam))
print("Egész szám: "+str(egeszSzam)+".")


# 1,b feladat
tortSzam = 2.5
# ellenőrzés
print(tortSzam)
print(type(tortSzam))
print("Tört szám: "+str(tortSzam)+".")

# 1,c feladat
szin = "zöld"
print(szin)
print(type(szin))
print("A kedvenc szinem a(z)", szin, ".")
print("A kevenc szinem a(z) "+szin+".")

# 1 d
betu = 'a'
print(betu)
print(type(betu))
print("Az ABC első betűje: "+betu+".")

# 1,e
szunetvanE = True
print(szunetvanE)
print(type(szunetvanE))

# 1,f
szunetvanE = False
print(szunetvanE)
print(type(szunetvanE))

# 2 feladat

szam = 4
fele = szam/2
print("A(z)"+str(szam)+" szám fel "+str(fele)+".")

# 3 Feladat

szam1 = int(input("Add meg az első valós számot: "))
szam2 = int(input("Add ,meg a második számot:  "))
szam3 = int(input("Add, meg a harmadik számot : "))

print("1. szám: "+str(szam1))
print("2. szám: "+str(szam2))
print("3. szám: "+str(szam3))

print("1. szám: "+str(szam1)+"\n2. szám: "+str(szam2)+"\n3. szám: "+str(szam3))


# 4 Feladat
# első megoldás
print("1. szám: "+str(szam1)+"\n2. szám: "+str(szam2)+"\n3. szám: "+str(szam3))

# második megoldás
print("1. szám: "+str(szam1), end="")
print("2. szám: "+str(szam2), end="")
print("3. szám: "+str(szam3))


# 5 Feladat

szam1, szam2 = 8, 2

osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1/szam2
maradek = szam1/szam2
hatvany = szam1**szam2

print(osszeg)
print(kulonbseg)
print(szorzat)
print(hanyados)
print(maradek)
print(hatvany)

# 6 Feladat


szam1, szam2 = 8, 2

osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1/szam2
hatvany = szam1**szam2
hatvany2 = szam1**szam2


print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1)+"-"+str(szam2)+"="+str(kulonbseg))
print(str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print(str(szam1)+"/"+str(szam2)+"="+str(hanyados))
print(str(szam1)+"%"+str(szam2)+"="+str(maradek))
print(str(szam1)+"^"+str(szam2)+"="+str(hatvany))
print(str(szam2)+"^"+str(szam1)+"="+str(hatvany2))

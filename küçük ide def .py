yazılacak_dosya = open("C:\\Users\Dogukan\Desktop\lovek .txt","w+")
okunacak_dosya = open(r"C:\Users\Dogukan\Desktop\text.txt")
isaret = ['{\n', '}\n', '{', '}']

def kücükide():
    bosluk_sayısı = 0
    b = []
    b += okunacak_dosya.readlines()
    indis = -1
    for i in b:
        indis += 1
        if i == isaret[1] or i == isaret[3]:
            bosluk_sayısı -= 4
        if i == isaret[0] or i == isaret[2]:
            bosluk_sayısı += 4
        if bosluk_sayısı != 0:
            b[indis] += '{}'.format(bosluk_sayısı * ' ')
    yazılacak_dosya.writelines(b)
kücükide()
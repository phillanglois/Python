import matplotlib.pyplot as plt
from points import ordre,comparaison
import random
def nuage(pts):
    x=[coord[0] for coord in pts]
    y=[coord[1] for coord in pts]
    plt.scatter(x,y)
    plt.show()

def partition(s, l, r, ordre):
    k = random.randint(l, r)
    s[k], s[r] = s[r], s[k]
    i = l - 1
    for j in range(l, r):
        if ordre(s[j], s[r]):
            i = i + 1
            s[i], s[j] = s[j], s[i]
    s[i + 1], s[r] = s[r], s[i + 1]
    return i + 1
def tri_part(s, l, r, ordre):
    if l <= r:
        q = partition(s, l, r, ordre)
        tri_part(s, l, q - 1, ordre)
        tri_part(s, q + 1, r, ordre)

def tri_rapid(s, ordre):
    tri_part(s, 0, len(s) - 1, ordre)
def tri_Angle(Omega, s):
    ordre = lambda A, B: comparaison(Omega, A, B)
    tri_rapid(s, ordre)    
def ecriture(nuage):
    fichier=open("nuage.txt","w")
    fichier.write(str(len(nuage)))
    fichier.write("\n")
    for i in range(len(nuage)):
        for j in range(len(nuage[0])):
            fichier.write(str(nuage[i][j])+"\t")
        fichier.write("\n")
    fichier.close()

def lecture(fichier):
    f=open(fichier,"r")
    for i in f:
        print(i)


def enregis(nuage):
    x=[coord[0] for coord in nuage]
    y=[coord[1] for coord in nuage]
    x.append(nuage[0][0])
    y.append(nuage[0][1])
    plt.plot(x,y,'k')
    plt.plot(x,y,'ro',markersize=6)
    plt.savefig("image1.jpeg")
    plt.show()
    plt.close()

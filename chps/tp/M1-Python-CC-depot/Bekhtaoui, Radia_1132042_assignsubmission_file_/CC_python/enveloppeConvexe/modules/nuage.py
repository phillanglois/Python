#il suffit alors d’utiliser la primitive import pour pouvoir utiliser ces fonctions
def definirNuage(x:list[float],y:list[float],t:int) -> list[tuple] :
    nuagePoint=list(zip(x,y))
    return nuagePoint 

def afficherNuage(x) :
    print(x)

def un_nuage_random(t:int) -> list[tuple] :
    x,y=[],[]
    for i in range(t) :
        x.append(uniform(0,1))
        y.append(uniform(0,1))
    n=definirNuage(x,y,t)
    return n

def trier_nuage(n:list[tuple],t:int) -> list[tuple]:
    n.sort()#respecte la relation d'ordre suivante entre 2 points
    return n

def write_nuage(t:int) :
    n=un_nuage_random(t)
    with open('data_nuage.txt', 'w') as f:
        f.write(f"{t}\n")
        for i in range(len(n)) :
            f.write(f"{n[i][0]} ")
            f.write(f"{n[i][1]}\n")

def read_nuage(fichier:str) -> list[tuple]:
    f = open(fichier, "r")
    x,y=[],[]
    t=int(f.readline()[:-1])
    i=t
    while i :
        i-=1
        thisLine=f.readline()[:-1].split()
        x.append(float(thisLine[0]))
        y.append(float(thisLine[1]))
    f.close()
    thisPoints=[]
    for j in range(len(x)):
        thisPoints.append(creerPoint(x[j],y[j]))   
    return thisPoints

def aff_nuage(points:list[tuple]):
    x,y=[],[]
    for i in range(len(points)) :
        x.append(points[i][0])
        y.append(points[i][1])
    plt.scatter(x,y,marker = 'o')
    plt.savefig("trace.jpeg")
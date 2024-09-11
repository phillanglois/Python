import point
def nuage_point(X:list[float],Y:list[float])->list[tuple[float]]:
    n=len(X)
    assert n==len(X)==len(Y)
    N=[]
    for i in range(n):
        N.append(point.definition_point(X[i],Y[i]))
    return N
import random
def nuage_aléatoire(n:int)->list[tuple[float]]:
    u=[]
    v=[]
    for i in range(n):
        u.append(random.uniform(0, 1))
        v.append(random.uniform(0, 1))
    return(nuage_point(u,v))

def trier_nuage(S:list[tuple[float]])->list[tuple[float]]:
    
    for i in range(len(S)):
        k=i
        for j in range(i+1,len(S)):
            if point.compare_point(S[j],S[k])==1:
                k=j
        x=S[i]
        S[i]=S[k]
        S[k]=x
    return S
def enregistrement_nuage(S:list[list[float]])->None:
    n=len(S)
    with open("nuage.txt", "w", encoding="utf8") as f:
        f.write( str(n) + '\n' )
        for i in range(n):
            f.write((str(S[i])) + '\n') 
        
def lire_nuage(S:list[list[float]])->None:
    n=len(S)
    with open("nuage.txt", "r", encoding="utf8") as f:
        n = int(f.readline()[:-1])
        for i in range(n):
            S[i]=tuple(f.readline()[:-1])
import matplotlib.pyplot as plt
def tracer_nuage(N:list[list[float]])->None: 
    X=[]
    Y=[]
    for i in range(len(N)):
        X.append(N[i][0])
        Y.append(N[i][1])
    plt.scatter(X,Y)
    plt.title('graphe du Nuage de points ')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('nuage_point.png')
    plt.show()


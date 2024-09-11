#il suffit alors d’utiliser la primitive import pour pouvoir utiliser ces fonctions
def creerPoint(x:float , y:float)-> tuple[float]:
    return(x,y)

def comparerPoint(a:tuple[float],b:tuple[float])->bool:
    if a[0]<b[0] or (a[0]==b[0] and a[1]<=b[1]):
        return True
    return False

def afficherPoint(a):
    print("coordonée du point:",a)
import matplotlib.pyplot as plt
from nuage import tri_Angle
from points import point_min
def orientation(p,q,r):
    vect_pq=(q[0]-p[0],q[1]-p[1])
    vect_pr=(r[0]-p[0],r[1]-p[1])
    det=vect_pq[0]*vect_pr[1]-vect_pq[1]*vect_pr[0]
    if det>0:
        return 1
    elif det<0:
        return -1
    else:
        return 0
def majES(point,pile=None):
    if pile is None:
        pile=[]
    mini_point=point_min(point)
    tri_Angle(mini_point,point)
    pile.append(point[0])
    pile.append(point[1])
    pile.append(point[2])
    for i in range(3,len(point)):
        while orientation(pile[-2],pile[-1],point[i])<0:
            pile.pop()
        pile.append(point[i])
    return pile
def majEI(point,pile=None):
    if pile is None:
        pile=[]
    mini_point=point_min(point)
    tri_Angle(mini_point,point)
    pile.append(point[0])
    pile.append(point[1])
    pile.append(point[2])
    for i in range(3,len(point)):
        while orientation(pile[-2],pile[-1],point[i])>0:
            pile.pop()
        pile.append(point[i])
    return pile
def Env_convexe(point):
    mini_point = point_min(point)
    tri_Angle(mini_point,point)
    n=len(point)
    EnvSup = []
    EnvInf = []
    for i in range(n):
        while len(EnvSup) >= 2 and orientation(point[i], point[EnvSup[-1]], point[EnvSup[-2]]) < 0:
            EnvSup.pop()
        EnvSup.append(i)
        while len(EnvInf) >= 2 and orientation(point[EnvInf[-2]], point[EnvInf[-1]], point[i]) < 0:
            EnvInf.pop()
        EnvInf.append(i)
    sommets = EnvInf[:-1] + EnvSup[::-1]
    return sommets
def affiche_enveloppe(point):
    #print(point)
    Enveloppe = Env_convexe(point)
    #print(Enveloppe)
    x = [point[i][0] for i in Enveloppe]
    x.append(point[Enveloppe[0]][0])
    y = [point[i][1] for i in Enveloppe]
    y.append(point[Enveloppe[0]][1])
    #plt.plot(x, y, "o-r") # PhL
    plt.plot(x, y)
    labels = ['$*$'.format(i) for i in range(len(point))]
    for label, x, y in zip(labels, [p[0] for p in point], [p[1] for p in point]):
        plt.annotate(label, xy=(x, y),  va='bottom', ha='right', size='large', color='black')
    
    plt.grid()
    plt.show()
def affiche_enveloppe_nuage(point):
    Enveloppe = Env_convexe(point)

    x = [point[i][0] for i in Enveloppe]
    x.append(point[Enveloppe[0]][0])
    y = [point[i][1] for i in Enveloppe]
    y.append(point[Enveloppe[0]][1])

    plt.subplot(211)
    plt.plot(x, y)
    plt.title("Enveloppe convexe ")

    labels = ['$*$'.format(i) for i in range(len(point))]
    for label, x, y in zip(labels, [p[0] for p in point], [p[1] for p in point]):
        plt.annotate(label, xy=(x, y),  va='bottom', ha='right', size='large', color='black')
    plt.grid(True)

    plt.subplot(212)
    plt.scatter([x for x,y in point], [y for x,y in point])
    plt.title("Nuage de points")
    plt.show()
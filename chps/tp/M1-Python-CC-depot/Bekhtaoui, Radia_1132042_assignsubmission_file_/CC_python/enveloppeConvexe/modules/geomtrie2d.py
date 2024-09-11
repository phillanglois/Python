#il suffit alors d’utiliser la primitive import pour pouvoir utiliser ces fonctions
def majES(pile:list[tuple], point:tuple)-> list[tuple]:
    pile.append(point)
    pileES=[]
    for p in reversed(pile):
        while len(pileES) >= 2 and orientation(pileES[-2],pileES[-1],p) <= 0:
            pileES.pop()
        pileES.append(p)
    pileES.reverse()
    return pileES

def majEI(pile:list[tuple], point:tuple)-> list[tuple]:
    pile.append(point)
    pileEI=[]
    for p in pile:
        while len(pileEI) >= 2 and orientation(pileEI[-2],pileEI[-1],p) <= 0:
            pileEI.pop()
        pileEI.append(p)
    return pileEI

def env_convexe(nuage:list[tuple])-> list:
    
    nuageTrie=trier_nuage(nuage,len(nuage))
    p0=nuageTrie[0]
    pn=nuageTrie[-1]
    
    convSup = majES(nuageTrie,pn)
    convInf = majEI(nuageTrie,pn)
    convInf.reverse()
    conv=convSup[:-1]+convInf[:-1]
    conv.append(p0)
    return conv

def print_env(env_conv:list[tuple]):
    print(env_conv)


def aff_nuage_env(nuage:list[tuple]):
    aff_nuage(nuage)#avec le nuage de points associé
    env_conv=env_convexe(nuage)
    axeX=[p[0] for p in env_conv]
    axeY=[p[1] for p in env_conv]
    plt.plot(axeX, axeY,marker = 'o')
   
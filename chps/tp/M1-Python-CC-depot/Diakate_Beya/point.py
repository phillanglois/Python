def definition_point(x:float,y:float)->tuple[float]:
    A=(x,y)
    return(A)
def compare_point(A:tuple,B:tuple)->int:
    if A[0]<B[0] or (A[0]==B[0] and A[1]<=B[1]):
            return 1# A plus petit que B
    else:
        return 0
def affiche_coordoonées(A:tuple[float])->float:
    return(A)
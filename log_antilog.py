poly_primitif=[1,3,7,13,23,45,103,203,435,1041,2011]
def conversion(x:int):
    x=str(x)
    chaine=''
    for i in x :
        chaine+= bin(int(i))[2:].zfill(3)
    chaine_finale=int(chaine,2)
    return chaine_finale

def gen_poly_primi():
    return [conversion(i) for i in poly_primitif]

gen_poly_primi()


poly_primitif=gen_poly_primi()
extension_degree =10
gf_cardinality= 2**extension_degree
gf_ord =gf_cardinality-1
gf_Antilog = [0 for i in range(gf_cardinality)]
gf_Log =[0 for i in range(gf_cardinality)]
def gf_antilog(extension_degree):    
    """ Fonction renvoyant la table exponentielle de Fp de degré d """
    poly, liste=poly_primitif[extension_degree], [0]*2**extension_degree
    liste[0] = liste[2**extension_degree-1] = 1 
    for i in range(1, 2**extension_degree):
        liste[i]=liste[i-1]<<1%256# equivaut  poly_ini = poly_ini << 1
        if liste[i] & 1<<extension_degree:
            liste[i] ^=poly
    return liste
gf_antilog(10)

def gf_log(d):
    return {key: value for (key, value) in zip(gf_antilog(d), range(15))}
gf_log(4)

def bezout(p,gf_ord): #fct récursive qui renvoie (g,x,y) tq ax+by=g (=pgcd(a,b))
    if p==0:
        return (gf_ord,0,1)
    else:
        g,y,x=bezout(gf_ord%p,p)
        return (g,x-(gf_ord//p)*y,y)
    
def invmod(a): #inverse modulaire de a modulo gf_ord
    g,x,y=bezout(a,gf_ord)
    if g!=1:
        raise Exception('pas inversible')
    else:
        return x%gf_ord

def carre(x):
    return gf_Antilog[(gf_Log[x]<<1) % gf_ord ]

    def xpow(x,pow):
    return gf_Antilog[(gf_Log[x]*pow) % gf_ord]
xpow(5,2)

def square_x(x):
    return gf_Antilog[(invmod(2)*(gf_Log[x]))%gf_ord]
square_x(2)

def division(x,y):
     return gf_Antilog[(gf_Log[x]-gf_Log[y])%15]
division(1,1)

def inverse(x):
    return division(1,x)
inverse(13)
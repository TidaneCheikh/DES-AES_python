import random
from random import*
s_box =[
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    ]

gen=[[hex(randint(0,15))[2:]+hex(randint(0,15))[2:] for i in range(4)] for j in range(4)]  
print(gen)
def createstate(state):
    return [[int(state[i][j],16)for i in range(4)]for j in range(4)]

def subBytes(s):
    s=createstate(s)
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]
    return [[hex(s[i][j])for i in range(4)]for j in range(4)]

se=[['53', '21', 'e2', '71'],
    ['31', '4b', '79', '23'], 
    ['6c', '79', 'fc', '5a'], 
    ['0a', 'e1', '59', '73']]

def shiftRows(state):
    s=createstate(state)
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    return [[hex(s[i][j])[2:]for i in range(4)]for j in range(4)]

def GF(a, b):
    a=int(a,16)
    b=int(b,16)
    r = 0
    for times in range(8):
        if (b & 1) == 1: 
            r = r ^ a
        if r > 0x100: 
            r = r ^ 0x100
        hi_bit_set = (a & 0x80)
        a = a << 1
        if a > 0x100:
            a = a ^ 0x100
        if hi_bit_set == 0x80:
            a = a ^ 0x1b
        if a > 0x100:
            a = a ^ 0x100
        b = b >> 1
        if b > 0x100:
            b = b ^ 0x100
    return r

def mixColums(s):
    t=[[0 for i in range(4)]for j in range(4)]
    for i in range(4):
        t[0][i]= GF('02',s[0][i])^GF('03',s[1][i])^GF('01',s[2][i])^GF('01',s[3][i])
        t[1][i] = GF('01',s[0][i])^GF('02',s[1][i])^GF('03',s[2][i])^GF('01',s[3][i])
        t[2][i] = GF('01',s[0][i])^GF('01',s[1][i])^GF('02',s[2][i])^GF('03',s[3][i])
        t[3][i] = GF('03',s[0][i])^GF('01',s[1][i])^GF('01',s[2][i])^GF('02',s[3][i])
    return [[hex(t[i][j])[2:]for i in range(4)]for j in range(4)]

def addroundkey(state,roundkey):
    state=createstate(state)
    roundkey=createstate(roundkey)
    for i in range(4):
        for j in range(4):
            state[i][j] ^=roundkey[i][j]
    return [[hex(state[i][j])[2:]for i in range(4)]for j in range(4)]
addroundkey(se,gen)

def subword(w):
    a0, a1, a2, a3 = w
    return s_box[a0[1]] +s_box[a1[1]] + s_box[a2[1]] + s_box[a3[1]]
    
def rotWord(w):
    (a0, a1, a2, a3) = wortToBytes(w)
    return a1 + a2 + a3 + a0

def rcon(n):
    RCON = ['01000000', '02000000', '04000000', '08000000','10000000', '20000000', '40000000', '80000000',
            '1b000000', '36000000']
    return RCON[n]

def keyToWords(key, Nk):
    keyWords = [[] for i in range(Nk)]
    word = 0
    tmp = ""
    for cpt in range(len(key)):
        if (cpt % 8 == 0) and (cpt <> 0):
            keyWords[word] = tmp
        word += 1
        tmp = key[cpt]
        else:
            tmp += key[cpt]
    keyWords[word] = tmp
    return keyWords

def keyExpansion(key, Nk=4, Nb=4, Nr=10):
    w = [0]*Nb*(Nr + 1)
    kw = keyToWords(key, Nk)
    for i in range(Nk):
        w[i] = kw[i]
    for i in range(Nk, Nb*(Nr + 1)):
        tmp = w[i-1]
        if (i % Nk == 0):
            tmp = int(subWord(rotWord(tmp)), 16) ^ int(rcon((i/Nk)-1), 16)
        elif ((Nk > 6) and (i % Nk == 4)):
            tmp = subWord(tmp)
        w[i] =int(w[i - Nk], 16) ^ int(tmp, 16)
    return w

def cipher(block, key, Nb=4, Nr=10):
    state = createstate(block, Nb)
    roundKey = "".join(key[0:Nb])
    state = addRoundKey(state, createState(roundKey, Nb), Nb)
    for round in xrange(1,Nr):
        state = subBytes(state, Nb)
        state = shiftRows(state, Nb)
        state = mixColumns(state, Nb)
        roundKey = "".join(key[round*Nb:(round*Nb)+Nb])
        state = addRoundKey(state, createState(roundKey, Nb), Nb)
        
    state = subBytes(state, Nb)
    state = shiftRows(state, Nb)
    roundKey = "".join(key[Nr*Nb:(Nr*Nb)+Nb])
    state = addRoundKey(state, createstate(roundKey, Nb), Nb)
    return createBlock(state, Nb)

def pgcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def eucli_etendu(a,b):
    u2, v2, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, u2, v2, b, u, v = b, u, v, a - q * b, u2 - q * u, v2 - q * v
    return ( u2, v2,a) if a > 0 else ( -u2, -v2,-a)

def inverse_entier(a,n):
    u,v,g=eucli_etendu(a,n)
    return u%n

def puissance_rapide(a,m,n):
    b=1
    e=[]
    m1=list(bin(m)[2:])
    [e.append(int(i)) for i in m1]
    e.reverse()
    k=len(e)
    if m==0:
        return b
    A=a
    if e[0]==1:
        b=a
    for i in range(k):
        A=(A**2)%n
        if e[i]==1:
            b=(A*b)%n
    return b
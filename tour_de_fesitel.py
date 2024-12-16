def keyGen(K):
    return [K[0] + K[2] + K[4] + K[6], Xor(K[0] + K[1] + K[4] + K[6], '1101')]

def fill(word, length):
    if len(word) < length:
        prefix = ''
        for i in range(length - len(word)):
            prefix += '0'
        word = prefix + word
    return word


def divider(m):
    return [m[:(len(m)//2)], m[(len(m)//2):]]

def Xor(A, B):
    AxorB = ''
    for i in range(len(A)):
        AxorB += str(int(A[i])^int(B[i]))
    return AxorB

def permutation(pi, word):
    newword = ''
    for i in pi:
        newword += word[i-1]
    return newword

def f(R, K):
    RXorK = fill(Xor(R,K), 4)
    S_de_RXorK = fill(bin(s[int(RXorK[0] + RXorK[3], 2)][int(RXorK[1:3], 2)])[2:], 4)
    pi = [4,2,3,1]
    pi_d_S_RXorK = permutation(pi, S_de_RXorK)
    return pi_d_S_RXorK

def feistel(L0, R0, K):
    L1 = R0
    R1 = Xor(L0, f(R0, K))
    return L1, R1

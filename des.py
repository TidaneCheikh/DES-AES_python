from random import*
import random
def genkey_system_DES(taille):
    return hex(int(''.join([random.choice(['0','1']) for i in range(0,taille)]),2))[2:]

def genkey_system(taille):
    if taille==64:
        return ''.join([hex(randint(0,15))[2:]+hex(randint(0,15))[2:] for i in range(8)])
    elif taille==128:
        return [[hex(randint(0,15))[2:]+ hex(randint(0,15))[2:] for i in range(4)] for j in range(4)]
    elif taille==192:
        return [[hex(randint(0,15))[2:]+ hex(randint(0,15))[2:] for i in range(4)] for j in range(6)]
    else :
        return [[hex(randint(0,15))[2:]+ hex(randint(0,15))[2:] for i in range(4)] for j in range(8)]

def genkey_subkeys_system_DES(key_64):
    round_shifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    L0,R0=div_key56(permut_56(p1,key_64))
    key=[]
    for i in range(16):
        L  =decalage(L0,round_shifts[i])
        R  =decalage(R0,round_shifts[i])
        key.append(compression_56(p2,L+R ))
        L0,R0=L,R
    return key

def cipher_system_DES(message,key):
    keys = genkey_subkeys_system(tranform_bin(key))
    L0,R0 =div_Mes(permuter(permutation_initial,tranform_bin(message)))
    for i in range(16):
        R1 =XOR(L0,f(R0,keys[i]))
        L1 =R0
        R0 =R1
        L0 =L1
    return hex(int(permuter(inv_permut,R0+L0),2))[2:]


p1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,
           23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
p2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,
    49,39,56,34,53,46,42,50,36,29,32]

def permut_56(p1,key_64):
    return ''.join([key_64[i-1] for i in p1])

def div_key56(keys_56):
    return keys_56[:28], keys_56[28:]

def decalage(b,n):
    return b[n:]+b[:n]

def compression_56(p2,keys_56):
    return ''.join([keys_56[i-1] for i in p2])

p_extension= [ 32 , 1 , 2 , 3 , 4 , 5 , 4 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 10 , 11 , 12 , 13 , 12 , 13 , 14 , 15 , 16 , 17 ,
16 , 17 , 18 , 19 , 20 , 21 , 20 , 21 , 22 , 23 , 24 , 25 , 24 , 25 , 26 , 27 , 28 , 29 , 28 , 29 , 30 , 31 , 32 , 1 ]

def Expansion(p,bits):
    return ''.join([bits[i-1] for i in p])

def  XOR(b1,b2):
    return ''.join(['0' if b1[i]==b2[i] else '1' for i in range((len(b1)))])

SBOX =[
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

import textwrap 
def  div_6bits(b):
    return  textwrap.wrap(b,6)

def debut_fin(b):
    return b[0]+b[-1]

def milieu_4(b):
    return b[1:5]

def bin_decimal(b):
    return int(b,2)

def decimal_bin(b):
    return bin(b)[2:].zfill(4)

def sbox(i,j,k):
    return decimal_bin(SBOX[i][bin_decimal(j)][bin_decimal(k)])

permu=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def Permute_sbox(p,sbox_32bi):
    return ''.join([sbox_32bi[i-1] for i in p])

def f(b,key48):
    r= ""
    bit=div_6bits(XOR(Expansion(p_extension,b),key48))
    for i, j in enumerate(bit):
        r+=sbox(i,debut_fin(j),milieu_4(j))
    return Permute_sbox(permu,r)

permutation_initial=['58 ' , '50' , '42 ' , '34' , '26 ' , '18' , '10 ' , ' 2 ' ,
'60', '52' , '44' , '36' ,'28', '20' ,'12', '4' ,'62' ,'54' ,'46', '38' ,'30' , '22' , '14' , '6' ,
'64' , '56' ,'48' ,'40', '32' , '24' , '16' , '8' ,'57' , '49' ,'41', '33', '25' , '17' , '9', '1' ,
 '59' , '51' ,'43','35','27' , '19' , '11', '3','61' , '53' ,'45','37','29' , '21' , '13' , '5' ,
 '63 ' , '55' , '47 ' , '39' , '31 ' , '23' , '15 ' , ' 7 ' ]

def tranform_bin(k):
    return ''.join([bin(int(i,16))[2:].zfill(4) for i in k])

def div_Mes(binaire):
    return binaire[:32],binaire[32:]

inv_permut=['40','8','48','16','56','24','64','32','39','7','47','15','55','23',
'63','31','38','6','46','14','54','22','62','30','37','5','45','13','53','21','61','29',
'36','4','44','12','52','20','60','28','35','3','43','11','51','19','59','27',
'34','2','42','10','50','18','58','26','33','1','41','9','49','17','57','25']

def permuter(p,r):
    return ''.join([r[int(i)-1] for i in p])

def cipher_system_DES(message,key):
    keys = genkey_subkeys_system_DES(tranform_bin(key))
    L0,R0 =div_Mes(permuter(permutation_initial,tranform_bin(message)))
    for i in range(16):
        R1 =XOR(L0,f(R0,keys[i]))
        L1 =R0
        R0 =R1
        L0 =L1
    return hex(int(permuter(inv_permut,R0+L0),2))[2:]

def decipher_system_DES(cipher,key):
    keys=genkey_subkeys_system_DES(tranform_bin(key))
    keys.reverse()
    R16,L16 =div_Mes(permuter(permutation_initial,tranform_bin(cipher)))
    for i in range(16):
        L1=XOR(R16,f(L16,keys[i]))
        R1=L16
        R16=R1
        L16=L1
    return hex(int(permuter(inv_permut,L16+R16),2))[2:]
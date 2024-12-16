import unidecode 
from random import*
def genkey_vigener(lon):
    key = []
    if lon<2:
        key.append(randint(0,25))
    else :
        taille = randint(2,(lon-1))
        for i in range(taille):
            key.append(randint(0,25))
    return key

def cipher_vigener(message,key):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    liste=[]
    message=message.upper()
    message=unidecode.unidecode(message)
    for i in message:
        if i in alphabet:
            liste.append(i)
    long=len(liste)
    t=len(key)
    textecode=""
    for k in range(long):
        j=k%t
        c=key[j]
        decalage=(c-97)-1
        textecode=textecode+chr((ord(liste[k])-97+decalage)%26+97)
    return textecode

from random import*
def genkey_vernam(lon):
    key = []
    for i in range(lon):
        i=randint(0,26)
        key.append(i)
    return key

def cipher_vernam(message,k):
    dico={}
    dico_inv={}
    alphabet= "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
    for i in range(26):
        dico_inv[i]=alphabet[i]
        dico[alphabet[i]]=i
    caract_message=[]
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    for i in range(len(accent)):
        message = message.replace(accent[i], sans_accent[i])
    message=message.upper()
    for i in message:
        if i in alphabet:
            caract_message.append(i)
    chiffre=[]
    liste=[]
    print(caract_message)
    print(dico)
    for élément in caract_message:
        for i in k:
            pos=dico[élément]+k[i]
            pos=pos%26
        chiffre.append(dico_inv[pos])  
    print("Le message chiffré est:")
    for i in chiffre:
         print(i,end="")


def genkey_affine():
     return [random.choice([1,3,5,7,9,11,15,17,19,21,25,23]),random.randint(0,25)]
    
# fonction de chiffrement affine
def cipher_Affine(message,cle):
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        liste=[]
        message=message.upper()
        message=unidecode.unidecode(message)
        for i in message:
            if i in alphabet:
                x=alphabet.index(i)
                y=(x*cle[0]+cle[1])%26
                liste.append(alphabet[y])
        liste="".join(liste)
        return liste
    
message=eval(input("entrer le message à chiffrer"))
cle=genkey_affine()
chiffre=cipher_Affine(message,cle)
print("le message chiffré est",chiffre)

def inverse(a):
        x=0
        while (a*x%26!=1):
                x=x+1
        return x
def decipher_Affine(chiffre,key):
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        liste=[]
        chiffre=chiffre.upper()
        chiffre=unidecode.unidecode(chiffre)
        for i in chiffre:
            if i in alphabet:
                c=alphabet.index(i)
                y=(key[0]*(c-key[1]))%26
                liste.append(alphabet[y])
        liste="".join(liste)
        return liste 

chaine=eval(input("entrer la chaine à dechiffrer"))
key=[inverse(cle[0]),cle[1]]
dechiffre=decipher_Affine(chaine,key)
print("le message dechiffré est :",dechiffre)

import random
def genkey_substitution():
    key =[]
    for i in range(26):
        key.append(i)
    random.shuffle(key)
    return key

def cipher_substitution(message,cle):
    dico={}
    dico_inv={}
    message=message.upper()
    alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste=[]
    for i in range(26):
        dico_inv[i]=alphabet[i]
        dico[alphabet[i]]=i
    for i,j in enumerate(alphabet):
        dico[j]=dico_inv[cle[i]]
    for i in message:
        liste.append(dico[i])
    liste="".join(liste)
    print("le dico de chiffrement est \n",dico)
    return liste
k=genkey_substitution()
print("la cle genereè \n",k)
a=eval(input("   "))
mes=cipher_substitution(a,k)
print("le message chiffré est \n",mes)

def decipher_substitution(chiffre,cle):
    dico={}
    dico_inv={}
    dico_i={}
    chiffre=chiffre.upper()
    alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste=[]
    for i in range(26):
        dico_inv[i]=alphabet[i]
        dico[alphabet[i]]=i
    for i,j in enumerate(alphabet):
        dico[j]=dico_inv[cle[i]]
    dico_inv = {v: k for k, v in dico.items()}
    print("dictionnaire de dechiffrement \n",dico_inv)
    for i in chiffre:
        liste.append(dico_inv[i])
    liste="".join(liste)
    return liste
b=eval(input("entrer le message a dechiffré \n"))
mess=decipher_substitution(b,k)
print(mess)



import sys
import numpy as np
import random as rnd
def genkey_hill():    
    while 1:
        a,b,c,d=[rnd.choice(range(1,26)) for i in range(4)]
        detA=(a*d-b*c)%26
        inv_detA=[i for i in range(1,26) if (i*detA)%26==1]
        if len(inv_detA)==1:
            break
    return [a,b,c,d]

def cipher_hill(message,key):
    message=message.upper()
    message=message.replace(" ","")
    len_ck=0
    if len(message)%2!=0:
        message=message+"A"
    row=2
    col=int(len(message)/2)
    mes=np.zeros((row,col),dtype=int)
    itr1=0
    itr2=0
    for i in range(len(message)):
        if i%2==0:
            mes[0][itr1]=int(ord(message[i])-65)
            itr1=itr1+1
        else :
            mes[1][itr2]=int(ord(message[i])-65)
            itr2=itr2+1
    print(key)
    key2=np.zeros((2,2),dtype=int)
    itr3=0
    for i in range(2):
        for j in range(2):
            key2[i][j]=key[itr3]-65
            itr3+=1
    print(key2)
    chiffre=""
    itr_count=int(len(message)/2)
    if len_ck==0:
        for i in range(itr_count):
            temp1=mes[0][i]*key2[0][0]+mes[1][i]*key2[0][1]
            chiffre=chiffre+chr((temp1%26)+65)
            temp2=mes[0][i]*key2[1][0]+mes[1][i]*key2[1][1]
            chiffre=chiffre+chr((temp2%26)+65)
    else :
         for i in range(itr_count-1):
            temp1=mes[0][i]*key2[0][0]+mes[1][i]*key2[0][1]
            chiffre=chiffre+chr((temp1%26)+65)
            temp2=mes[0][i]*key2[1][0]+mes[1][i]*key2[1][1]
            chiffre=chiffre+chr((temp2%26)+65)
    return chiffre     
message=input("entrer un message \n ")  
key=genkey_hill()
a=cipher_hill(message,key)
print(a)

def decipher_hill(message,key):
    message=message.upper()
    message=message.replace(" ","")
    len_ck=0
    if len(message)%2!=0:
        message=message+"A"
    row=2
    col=int(len(message)/2)
    mes=np.zeros((row,col),dtype=int)
    itr1=0
    itr2=0
    for i in range(len(message)):
        if i%2==0:
            mes[0][itr1]=int(ord(message[i])-65)
            itr1=itr1+1
        else :
            mes[1][itr2]=int(ord(message[i])-65)
            itr2=itr2+1
    key2=np.zeros((2,2),dtype=int)
    itr3=0
    for i in range(2):
        for j in range(2):
            key2[i][j]=key[itr3]-65
            itr3+=1
    dechiffre=""
    itr_count=int(len(message)/2)
    if len_ck==0:
        for i in range(itr_count):
            temp1=mes[0][i]*key2[0][0]+mes[1][i]*key2[0][1]
            dechiffre=dechiffre+chr((temp1%26)+65)
            temp2=mes[0][i]*key2[1][0]+mes[1][i]*key2[1][1]
            dechiffre=dechiffre+chr((temp2%26)+65)
    else :
         for i in range(itr_count-1):
            temp1=mes[0][i]*key2[0][0]+mes[1][i]*key2[0][1]
            dechiffre=dechiffre+chr((temp1%26)+65)
            temp2=mes[0][i]*key2[1][0]+mes[1][i]*key2[1][1]
            dechiffre=dechiffre+chr((temp2%26)+65)
    return dechiffre
text=input("entrer le texte a dechiffrer:\n")
b=decipher_hill(text,key)
print(b)


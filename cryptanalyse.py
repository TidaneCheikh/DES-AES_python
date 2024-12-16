def freq_alph(message):
    nombre_de_lettres={}
    message=message.upper()
    lon=len(message)
    for char in message:
        if char not in  nombre_de_lettres:
            nombre_de_lettres[char]=1
        else :
            nombre_de_lettres[char]=nombre_de_lettres[char]+1
    for  i in nombre_de_lettres:
        nombre_de_lettres[i]=(nombre_de_lettres[i]/lon)*100
    return nombre_de_lettres
message=input("le texte:\n")
q=freq_alph(message)
print("\nLa frequence des nombres:\n",q)
print("\nD'apres la frequence des lettres , les plus elevés sont l'espace et la lettre K on suppose donc que K est la lettre E ")
print("\nComme A et S sont compris entre 8% et 10%: on suppose donc que soit A=R ou S=R mais dans le texte chiffré la lettre R est souvent a la fin des mots il est plus probable que S soit egal à R, on admet dans ce cas que S=R")
print("\nOn a deux lettre dont frequence est superieur à 6.3 qui sont P et G les lettres qui entrent en jeux sont: A I N T, Mais remarquons que dans le message chiffré la lettre G est souvent seule or en francais y'a que la lettre A et Y qui peuvent etre seule comme Y a une frequene faible donc G=A , Maintenant pour P dans le cipher on a un KP , on exclu le fat que P=I on n pourrait avoir le mot 'ei' ,soit P=N ou P=T or on voit un QP dans le texte 'ut' et 'ot' nexiste pas en francais d'ou P=N")
print("\nOn 4 lettres de plus de 4.5% I J U M ,les lettres concernes sont O L I U   ou T , dans le texte il ya un PJP comme  P=N on suppose que J=O,on a un KI comme K=E et I=T , U est entre deux K=E : U ne peut etre une voyelle  U=R,M est entre deux consonnes donc M=I ou M=I, posons M=I")
print("\nH X W Q Z  sont entre 2.5 et 4.5 qui correspond au lettres C M P D et U")
print("\nOn voit dans le cipher un JQ , J=0 donc Q=U")
print("\nEn suivant ce logique et en remplacant petit a petit les lettres trouvés et de la connaissance qu'on a des mots en francas,on parvient a completement le texte ")
message=message.replace("K","e")
message=message.replace("R","s")
message=message.replace("G","a")
message=message.replace("P","n")
message=message.replace("J","o")
message=message.replace("I","t")
message=message.replace("Q","u")
message=message.replace("M","i")
message=message.replace("X","m")
message=message.replace("P","p")
message=message.replace("W","c")
message=message.replace("S","q")
message=message.replace("D","l")
message=message.replace("U","r")
message=message.replace("N","y")
message=message.replace("H","p")
message=message.replace("Z","d")
message=message.replace("V","g")
message=message.replace("A","v")
message=message.replace("Y","x")
message=message.replace("B","f")
message=message.replace("O","b")
message=message.replace("F","h")
print("\n le message dechiffré est:\n",message)


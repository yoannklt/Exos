#DEBUT

#premier exercice
#r = 12000
#s = 1250
#e = 10
#rh = 230
#assertionFinale = (( (365 * 3) / (24 -(16 -8)) ) * (rh) > r) == (e * s < r)

#premiereAssertion = (( (365 * 3) / (24 -(16 -8)) ) * (rh) > r) = ( 1095 / (24 - 8) * 230 > 12000) = ( 1095 / 16 * 230 > 12000) = (15740.625 > 12000) #True
#deuxiemeAssertion = (e * s < r) = (10 * 1250 < 12000) = (12500 < 12000) #False
#assertionFinale = premiereAssertion == deuxiemeAssertion #False

#deuxieme exercice
#assertionFinaleDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) == (e *s < r)

#premiereAssertionDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) = (1095 / 0 * 230 > 12000) #False
#deuxiemeAssertionDeux = (e *s < r) = (10 * 1250 < 12000) = (12500 < 12000) #False
#assertionFinaleDeux = premiereAssertionDeux == deuxiemeAssertionDeux #True
#

# def input():
        # "oeoeoe"
#Renvoie un caractère de type str au hasard

#Exercice:
    #Faire un mini-jeu qui affiche un message lorsque input renvoie le bon caractère
    #Le caractère doit être parametrable

#def miniJeu(resultLetter): 
#    if resultLetter != input("C'est quoi la lettre khoya ?"):
#        print("C'est perdu")
#        return miniJeu(resultLetter) + 1
#    else :
#        print("C'est gagné")
#       return 1
    
#print(miniJeu("e"))

prenom = "Yoann"
nom = "Kerlogot"
#identite = nom + " " + prenom  #retourne "Kerlogot Yoann"

integerValue = 342 #Retourne 342
stringIntegerValue = str(342) #Retourne "342"

#tableau = [0,10,15,5,1]
#Pour récupérer 15 je prends dans tableau l'index 2

#print(tableau[2]) #Affiche 15

#Exercice 1
#Faire une fonction qui concatene 2 chaines de caractères, les séparants par une virgule

def concatWithComma(strA, strB):
    stringifiedA = str(strA)
    stringifiedB = str(strB)
    return stringifiedA + ", " + stringifiedB

#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractère avec l'ensemble des occurences d'un chiffre
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction (tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas à implémenter la première fonction 
tableau = [0,1,1,1,0,1,1,0,1]
#Définir la fonction findIndex qui itère sur tableau, cherchant l'index
#Des différentes occurences de x
def findIndex(tableau, x) :
    #Définir un index de départ
    i = 0
    #Je définie un boolean tel que firstTurn est true
    firstTurn = True
    #Définir chaineRetour telle qu'une chaine de caractère vide
    chaineRetour = ''
    #Tant que i est différent du nombre d'elt dans le tableau 
    while (i != len(tableau)):
        #Alors j'attribue a une variable la valeur de tableau à l'index i
        selected = tableau[i]
        #Si selected est égal à x et que firstTurn est true
        if selected == x and firstTurn :
            #Alors on assigne à chaineRetour le retour de str(i)
            chaineRetour = str(i)
            #Changer la valeur de firstTurn en False
            firstTurn = False
        #Sinon si selected est égale à x
        elif selected == x :
            #Alors j'assigne le retour de  concatWithComma tel que: concatWith Comma (chainerRetour, i) à chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
        #J'incrémente i de 1
        i = i + 1
    #Retourner la chaine retour
    return chaineRetour     

print(findIndex(tableau, 0))

#Exercice 3
#Renvoyer/Afficher un message

print("un message")

#Définir la fonction suiteFibonacci qui itère sur debutSuite, cherchant l'index
#Des différentes occurences de x

#FIN
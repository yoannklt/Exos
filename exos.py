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
x = 4
y = 2

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y


def salaireNet(brut, coéfficient):
    return brut * coéfficient

def salaireParSeconde(salaireHoraire, heuresParJourOuvré, nbDeJoursOuvrésParAn):
    return (salaireHoraire * heuresParJourOuvré * nbDeJoursOuvrésParAn) / (60 * 60 * 24 * 365)

print(salaireParSeconde(12, 7, 235))

def SalaireParSeconde(salaireHoraire, heuresParJourOuvré, jourOuvreParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heuresParJourOuvré * jourOuvreParAn
    #Calculer le nombre de seconde dans une année
    nbSecondeParAn = 365 * 24 * 60 * 60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondeParAn
    
#FIN
#Radu Cosmin 323 CB
#@cosminr47 - utilizator pe hackerrank

import sys
import itertools

#Functie pentru sortarea matricii variabilelor si cea a aparitiei variabilelor
#simultan
def sortare_matr(matrice_var, matrice_apar):
    for i in range(0, len(matrice_var)):
        for j in range(0, len(matrice_var[i]) - 1):
            for k in range(0, len(matrice_var[i]) - j - 1):
                if matrice_var[i][k] > matrice_var[i][k + 1]:
                    aux = matrice_var[i][k]
                    aux_apar = matrice_apar[i][k]
                    matrice_var[i][k] = matrice_var[i][k + 1]
                    matrice_apar[i][k] = matrice_apar[i][k + 1]
                    matrice_var[i][k + 1] = aux
                    matrice_apar[i][k + 1] = aux_apar

#Functie care transforma formula in matrice pentru a fi utilizata ulterior
def convert(string):
    #max_vars retine numarul maxim de variabile dintr-o clauza
    max_vars = 0
    #matricea ce contine variabilele pe fiecare rand
    matrice_var = []
    #matricea ce contine -1/0/1 in functie de cum e prezenta variabila in clauza
    matrice_apar = []
    for c in string.split('^'):
        nr_vars = 0
        #Se creeaza cate o lista pentru variabile si prezenta lor in clauze
        variables = []
        neg = []
        for var in c.split('V'):
            #Se elimina simbolurile suplimentare, iar daca apare si negatia
            #se retine -1 
            var = var.replace('(', '')
            var = var.replace(')', '')
            if var[0] == '~':
                neg.append(-1)
                var = var.replace('~', '')
            else:
                neg.append(1)
            #Se adauga variabila in lista ca intreg
            variables.append(int(var))
            nr_vars += 1
        #Se adauga in fiecare matrice listele create
        matrice_apar.append(neg)
        matrice_var.append(variables)
        #Se va retine in l_pivot lista care contine toate variabilele
        if nr_vars > max_vars:
            max_vars = nr_vars
            l_pivot = variables
    #Pentru a reduce numarul de operatii efectuate, se calculeaza o singura
    #data lungimea listei si numarul de clauze din formula
    lung_matr = len(matrice_var)
    lung_ref = len(l_pivot)
    for i in range(0, lung_matr):
        if len(matrice_var[i]) != lung_ref:
            for j in range(0, lung_ref):
                #Daca o variabila nu e prezenta in clauza curenta, este adaugat
                #0 in matricea ce contorizeaza prezenta si pe ea insasi in
                #clauza
                if l_pivot[j] not in matrice_var[i]:
                    matrice_var[i].append(l_pivot[j])
                    matrice_apar[i].append(0)
    #Sunt sortate simultan cele doua matrice si se returneaza cea care
    #contorizeaza prezenta
    sortare_matr(matrice_var, matrice_apar)
    return matrice_apar

#Functia care rezolva problema SAT, utilizand matricea
def fnc(matrice):
    #Se genereaza toate interpretarile posibile de lungime egala ca numarul de
    #variabile
    combinatii = list(map(list, itertools.product([0, 1],
        repeat=len(matrice[0]))))
    nr_combinatii = len(combinatii)
    i = 0
    while i != nr_combinatii:
        eval_combinatie = True
        partial = False
        lungime = len(matrice)
        for j in range(0, lungime):
            lungime_linie = len(matrice[j])
            for k in range(0, lungime_linie):
                #Daca variabila nu e prezenta in clauza, se trece la urmatoarea
                if matrice[j][k] == 0:
                    continue
                #Daca o variabila are valoarea 1, clauza are valoarea 1 si
                #se evalueaza urmatoarea
                if matrice[j][k] == 1 and combinatii[i][k] == 1:
                    partial = True
                    break
                if matrice[j][k] == -1 and combinatii[i][k] == 0:
                    partial = True
                    break
            #Daca valoarea unei clauze este 0, valoarea expresiei pentru acea 
            #interpretare este 0.
            #Astfel, se trece la urmatoarea interpretare
            if partial == False:
                eval_combinatie = False
                break
            partial = False
        #Daca pentru o interpretare formula este adevarata, se printeaza
        #rezultatul si se intoarce 1
        if eval_combinatie == 1:
            print(1)
            return 1
        i += 1
    #Daca nu s-a gasit o interpretare care sa satisfaca formula, se intoarce 0
    return 0

#Se extrage de la stdin formula
while True:
    try:
        formula = input();
    except EOFError:
        break
#Paranteza finala se pierde din cauza prezentei EOF
formula += ')'
#Se obtine matricea necesara pentru solver
matrix = convert(formula)
#In cazul in care functia intoarce 0, se printeaza 0
if fnc(matrix) == 0:
    print(0)
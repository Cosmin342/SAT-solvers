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
    matr_vars = []
    #matricea ce contine -1/0/1 in functie de cum e prezenta variabila in clauza
    neg_vars = []
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
        neg_vars.append(neg)
        matr_vars.append(variables)
        #Se va retine in l_pivot lista care contine toate variabilele
        if nr_vars > max_vars:
            max_vars = nr_vars
            l_pivot = variables
    #Pentru a reduce numarul de operatii efectuate, se calculeaza o singura
    #data lungimea listei si numarul de clauze din formula
    lung_matr = len(matr_vars)
    lung_ref = len(l_pivot)
    for i in range(0, lung_matr):
        if len(matr_vars[i]) != lung_ref:
            for j in range(0, lung_ref):
                #Daca o variabila nu e prezenta in clauza curenta, este adaugat
                #0 in matricea ce contorizeaza prezenta si pe ea insasi in
                #clauza
                if l_pivot[j] not in matr_vars[i]:
                    matr_vars[i].append(l_pivot[j])
                    neg_vars[i].append(0)
    #Sunt sortate simultan cele doua matrice si se returneaza cea care
    #contorizeaza prezenta
    sortare_matr(matr_vars, neg_vars)
    return neg_vars

#Functia care rezolva problema SAT, utilizand reprezentarea BDD
def bdd(matrix):
	#Arborele este stocat intr-o lista, ca la un heap
	arb = [matrix]
	#current retine pozitia variabilei curente
	current = 0
	#par este o variabila folosita pentru a determina daca variabila curenta
	#trebuie folosita cu valoarea 0 sau 1
	par = 0
	lung = len(matrix[0])
	while True:
		#Daca pozitia variabilei curente este mai mare sau egala cu 1, se
		#copiaza matricea nodului parinte in m
		if current >= 1:
			aux = arb[int(len(arb) / 2)]
			m = aux[:]
		#Altfel, se copiaza matricea originala
		else:
			m = matrix[:]
		i = 0
		while 1:
			#Daca se ajunge la ultima linie a matricei, bucla se opreste
			if i == len(m):
				break
			#Daca par este un numar par, variabila curenta se foloseste cu
			#valoarea 0 (False)
			if par % 2 == 0:
				#Daca elementul curent din matrice e -1, linia este satisfacuta,
				#prin urmare eliminata
				if m[i][current] == -1:
					m.pop(i)
					continue
			#Altfel, se elimina o linie daca elementul curenta din ea este 1
			#si cand par este impar
			else:
				if m[i][current] == 1:
					m.pop(i)
					continue
			i += 1
		#Matricea creata este pusa in arbore
		arb.append(m)
		#Daca aceasta este goala, inseamna ca s-a gasit o interpretare care
		#satisface formula, iar programul se opreste
		if m == []:
			print(1)
			return 1
		par += 1
		#Daca par este patrat perfect, diferit de 1, se trece la urmatoarea
		#variabila pentru evaluarea SAT
		if par & (par - 1) == 0:
			if par != 1:
				current += 1
		#Daca se depaseste numarul maxim de variabile, bucla se incheie
		if current >= lung:
			break
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
if bdd(matrix) == 0:
    print(0)
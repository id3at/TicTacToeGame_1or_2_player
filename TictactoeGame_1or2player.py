"""
Autor id3at
Gra w kolko krzyzyk
+gra z komputerem
"""
import os

odpow = input('Wybierz. Gra jednosobowa "1", gra na dwóch "2"')
gra = [['…', '…', '…'],
       ['…', '…', '…'],
       ['…', '…', '…']]

suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
c = [t[0] for t in gra]
d = [t[1] for t in gra]
e = [t[2] for t in gra]
przekotna1 = [gra[i][i] for i in range(3)]
przekotna2 = [gra[i][2-i] for i in range(3)]
wszy = [c,d,e]


#########################################
def tablica():
    print('   0     1    2')
    for x, y in  enumerate(gra):
        print(x, y)
##########################################
print('''Gra kolko krzyzyk.
Pusta plansza\n''')
tablica()
print('''\n
Wprowadzanie krzyzyka "X" polega na wybraniu
przez gracza nr. rzedu np. "1" i nr.  kolumny np. "1".
Przykladowo wybor "11" zmieni plansze tak.
''')
print('   0     1    2')
for x, y in  enumerate(gra):
    if y[1] == '…':
        gra[1][1] = 'X'
    print(x, y)
print('\n')
gra[1][1] = '…'
##################################################################
print('Zacznijmy grę.\n')
tablica()
print('\n')
##################################################################
def checttt(gra):
    """ Funkcja sprawdzajaca wygrana w grze."""
    wyg = []
    c = [t[0] for t in gra]
    d = [t[1] for t in gra]
    e = [t[2] for t in gra]
    przekotna1 = [gra[i][i] for i in range(3)]
    przekotna2 = [gra[i][2-i] for i in range(3)]
    for t in range(3):
        if gra[t].count('X') == 3:
            wyg.append('X wygral')
        elif gra[t].count('O') == 3:
            wyg.append('O wygral')
    for s in ['X', 'O']:
        if c.count(s) == 3:
            wyg.append(f'{s} wygral')
        elif d.count(s) == 3:
            wyg.append(f'{s} wygral')
        elif e.count(s) == 3:
            wyg.append(f'{s} wygral')
        elif przekotna1.count(s) == 3:
            wyg.append(f'{s} wygral')
        elif przekotna2.count(s) == 3:
            wyg.append(f'{s} wygral')
    return wyg
##################################################################
def tictactoe(wejscie, wartosc):
    """Funkcja pobierajaca dane od uzytkownika."""
    war = []
    #os.system('cls')
    while len(war) == 0:
        wejscieint = [int(t) for t in wejscie]
        if  gra[wejscieint[0]][wejscieint[1]] == '…':
            gra[wejscieint[0]][wejscieint[1]] = wartosc
            war.append(1)
            tablica()
        else:
            print(f'Miejsce "{wejscie}" jest zajete, wybierz inne miejsce dla {wartosc}')
            tablica()
            wejscie = input(f'Gdzie wprowadzić {wartosc}?: ')
##################################################################
"""
wstepna logika komputera gry w kolko krzyzyk
dla dwóch miejsc zajętych
"""
def logikakom(x, y, z):
    zbior = []
    c = [t[0] for t in gra]
    d = [t[1] for t in gra]
    e = [t[2] for t in gra]
    przekotna1 = [gra[i][i] for i in range(3)]
    przekotna2 = [gra[i][2-i] for i in range(3)]
    wszy = [c,d,e]

    for l, t in enumerate(wszy):
        #if gra[1][1] == '…':
        #  gra[1][1] = 'O'
        
        if gra[l].count(x) == 2 and gra[l].count(y) == 1:
            lic = gra[l].index(y)
            gra[l][lic] = z
            zbior.append(l)
            break
        elif t.count(x) == 2 and t.count(y) ==1:
            lic=t.index(y)
            gra[lic][l] = z
            zbior.append(l)
            break
        elif przekotna1.count(x) == 2 and przekotna1.count(y) == 1:
            lic = przekotna1.index(y)
            gra[lic][lic] = z
            zbior.append(l)
            break
        elif przekotna2.count(x) == 2 and przekotna2.count(y) == 1:
            lic = przekotna2.index(y)
            gra[lic][2-lic] = z
            zbior.append(l)
            break
    return zbior
"""
logika dla dwoch pustych miejs i jednego zajetego
"""
def logikakom2(x, y, z):
    zbior = []
    c = [t[0] for t in gra]
    d = [t[1] for t in gra]
    e = [t[2] for t in gra]
    przekotna1 = [gra[i][i] for i in range(3)]
    przekotna2 = [gra[i][2-i] for i in range(3)]
    wszy = [c,d,e]
    for l, t in enumerate(wszy):
        if przekotna1.count(x) == 2 and przekotna1.count(y) == 1:
            lic = przekotna1.index(x)
            gra[lic][lic] = z
            zbior.append(l)
            break
        elif przekotna2.count(x) == 2 and przekotna2.count(y) == 1:
            lic = przekotna2.index(x)
            gra[lic][2-lic] = z
            zbior.append(l)
            break
        elif gra[l].count(x) == 2 and gra[l].count(y) == 1:
            lic = gra[l].index(x)
            gra[l][lic] = z
            zbior.append(l)
            break
        elif t.count(x) == 2 and t.count(y) ==1:
            lic=t.index(x)
            gra[lic][l] = z
            zbior.append(l)
            break



    return zbior
###########################################################
iksy = []
kolka = []

if odpow == '2': 
    while suma > 0:
        try:
            suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
            
            if suma > 0:
                if len(iksy) == len(kolka):
                    wejscie = input('Gdzie wprowadzic "X"?: ')
                    wartosc = 'X'
                    tictactoe(wejscie, wartosc)
                    iksy.append(wejscie)
            if len(checttt(gra)) == 1:
                print(checttt(gra))
                break
        except:
            print("Prosze wpisac dwie cyfry, zlozone z liczb od 0 do 2 np '01'")
            tablica()
        try:    
            suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
            if suma > 0: 
                if len(iksy) > len(kolka): 
                    wejscie2 = input('Gdzie wprowadzic "O"?: ')
                    
                    wartosc2 = 'O'
                    tictactoe(wejscie2, wartosc2)
                    kolka.append(wejscie2)
            if len(checttt(gra)) == 1:
                print(checttt(gra))
                break
            suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
    
        except:
            print("Prosze wpisac dwie cyfry, zlozone z liczb od 0 do 2 np '01'")
            tablica()
else:
    while suma != 1:
        try:
            suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
            if suma > 0:
                wejscie = input('Gdzie wprowadzic "X"?: ')
                wartosc = 'X'
                tictactoe(wejscie, wartosc)
            if len(checttt(gra)) == 1:
                print(checttt(gra))
                break
            while True:
                suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
                if gra[1][1] == '…':
                    gra[1][1] = 'O'
                    break
                elif   len(logikakom('O', '…', 'O')) == 1:
                    break
                elif len(logikakom('X', '…', 'O')) == 1:
                    break
                elif len(logikakom2('…', 'X', 'O')) == 1:
                    break
            if len(checttt(gra)) == 1:
                print(checttt(gra))
                break
            tablica()
            suma = gra[0].count('…')+gra[1].count('…')+gra[2].count('…')
            if suma == 1:
                print("Remis")
                break
        except:
            print("Prosze wpisac dwie cyfry, zlozone z liczb od 0 do 2 np '01'")
            tablica()

input('Koniec gry! Nacisnij Enter!')

import os

CESTA_K_MINISAT = "minisat"

N = 0

# Pomocna funkcia na zapis implikacie do suboru
def impl(subor, a, b):
    subor.write( "{0:d} {1:d} 0\n".format(-a, b) )

def q(i,j):
    return i*N + j +1
# Funkcia zapisujuca problem do vstupneho suboru SAT solvera v spravnom formate
def zapis_problem(subor):
    # V kazdom riadku je aspon jedna dama
    for i in range(N):
        for j in range(N):
            subor.write("{0:d} ".format( q(i,j)) )
        subor.write("0\n")
    # V kazdom riadku je najciac jedna dama
    for i in range(N):
        for j1 in range(N):
            for j2 in range(N):
                if j1!= j2:
                    impl(subor, q(i,j1), -q(i,j2))
    
    # V kazdom strlpci je najviac jedna dama
    for i in range(N):
        for j1 in range(N):
            for j2 in range(N):
                if j1!= j2:
                    impl(subor, q(i,j1), -q(i,j2))
        
    # Na kazdej uhlopriecke je jedna dama


# Funkcia vypisujuca riesenie najdene SAT solverom z jeho vystupneho suboru
def vypis_riesenie(ries):
    # rozbijeme riesenie na cisla/premenne
    vs = ries.split()
    # zahodime ukoncovaciu 0
    vs = vs[0:-1]
    # vypiseme vyznam riesenia
    for v in vs:
        v = int(v)
        print(v)
        #print("{0} {1}pojde na party".format(
        #        intToName[abs(v)],
        #        "ne" if v < 0 else ""))

def main():
    # Normalne by sme tu mozno nieco nacitavali zo standardneho vstupu,
    # ale tato uloha nema ziadny vstup.

    global N
    N = int(input())
    
    # otvorime subor, do ktoreho zapiseme vstup pre sat solver
    try:
        with open("vstup.txt", "w") as o:
            # zapiseme nas problem
            zapis_problem(o)
    except IOError as e:
        print("Chyba pri vytvarani vstupneho suboru ({0}): {1}".format(
                e.errno, e.strerror))
        return 1

    # spustime SAT solver
    os.system("{} vstup.txt vystup.txt".format(CESTA_K_MINISAT));

    # nacitame jeho vystup
    try:
        with open("vystup.txt", "r") as i:
            # prvy riadok je SAT alebo UNSAT
            sat = i.readline()
            if sat == "SAT\n":
                print("Riesenie:")
                # druhy riadok je riesenie
                ries = i.readline()
                vypis_riesenie(ries)
            else:
                print("Ziadne riesenie")
    except IOError as e:
        print("Chyba pri nacitavani vystupneho suboru ({0}): {1}".format(
                e.errno, e.strerror))
        return 1

    return 0

if __name__ == "__main__":
    main()

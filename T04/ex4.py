# Àlex Tasias

import sys
import argparse

def mostrar_ajuda():
    print("""
Ús: python ex4.py fitxer [c] [-i -p -P -f] [--help]

Arguments:
  fitxer   -> Fitxer de text a llegir.
  c        -> Caràcter per filtrar.
  -i       -> Compta les línies que NO contenen el caràcter.
  -p       -> Compta les línies que comencen pel caràcter.
  -P       -> Compta les línies que acaben pel caràcter (no compta \\n).
              (No es pot usar -p i -P alhora)
  -f       -> Escriu el resultat al fitxer 'sortida.txt'.
  --help   -> Mostra aquesta ajuda.

Exemples:
  python ex4.py arxiu.txt
  python ex4.py arxiu.txt a
  python ex4.py arxiu.txt a -p
  python ex4.py arxiu.txt a -i -P -f
""")

def comptar_línies(fitxer, c=None, negatiu=False, inici=False, final=False):
    try:
        with open(fitxer, 'r', encoding='utf-8') as f:
            total = 0
            for linia in f:
                linia = linia.rstrip('\n')
                ok = True

                if c:
                    if inici:
                        ok = linia.startswith(c)
                    elif final:
                        ok = linia.endswith(c)
                    else:
                        ok = c in linia

                    if negatiu:
                        ok = not ok

                if ok:
                    total += 1

            return total

    except FileNotFoundError:
        print(f"Error: El fitxer '{fitxer}' no existeix.")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        print("Error: No s'han donat arguments. Usa --help per veure com funciona.")
        sys.exit(1)

    if sys.argv[1] == "--help":
        mostrar_ajuda()
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("fitxer")
    parser.add_argument("caracter", nargs='?')
    parser.add_argument("-i", action="store_true")
    parser.add_argument("-p", action="store_true")
    parser.add_argument("-P", action="store_true")
    parser.add_argument("-f", action="store_true")
    args = parser.parse_args()

    if args.p and args.P:
        print("Error: No pots posar -p i -P alhora.")
        mostrar_ajuda()
        sys.exit(1)

    if (args.i or args.p or args.P) and not args.caracter:
        print("Error: Necessites un caràcter per usar -i, -p o -P.")
        mostrar_ajuda()
        sys.exit(1)

    resultat = comptar_línies(
        args.fitxer,
        c=args.caracter,
        negatiu=args.i,
        inici=args.p,
        final=args.P
    )

    if args.f:
        with open("sortida.txt", "w", encoding='utf-8') as sortida:
            sortida.write(f"Resultat: {resultat}\n")
    else:
        print(f"Resultat: {resultat}")

if __name__ == "__main__":
    main()

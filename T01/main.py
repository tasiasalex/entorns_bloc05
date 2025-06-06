def introduir_int_segur(text, min_val=None, max_val=None):
    """
    Demana un enter a l'usuari, validant que estigui dins del rang opcional.

    Args:
        text (str): Missatge per a l'input.
        min_val (int, optional): Valor mínim permès.
        max_val (int, optional): Valor màxim permès.

    Returns:
        int: Valor enter vàlid introduït per l'usuari.

    NOTA: No es pot fer doctest per aquesta funció perquè demana input.
    """
    while True:
        try:
            valor = int(input(text))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"Introdueix un nombre entre {min_val} i {max_val}.")
            else:
                return valor
        except ValueError:
            print("Introdueix un valor sencer vàlid.")

def comptar_majuscules_minuscules(cadena):
    """
    Compta les majúscules i minúscules d'una cadena.

    Args:
        cadena (str): Text d'entrada.

    Returns:
        tuple: (nombre de majúscules, nombre de minúscules)

    Examples:
        >>> comptar_majuscules_minuscules('Una Cadena De Prova')
        (4, 12)
        >>> comptar_majuscules_minuscules('A')
        (1, 0)
        >>> comptar_majuscules_minuscules('a')
        (0, 1)
    """
    majuscules = sum(1 for c in cadena if c.isupper())
    minuscules = sum(1 for c in cadena if c.islower())
    return majuscules, minuscules

def calcular_any_traspas(any):
    """
    Comprova si un any és de traspàs.

    Args:
        any (int): L'any a comprovar

    Returns:
        bool: True si és de traspàs, False si no ho és

    Examples:
        >>> calcular_any_traspas(2000)
        True
        >>> calcular_any_traspas(1900)
        False
        >>> calcular_any_traspas(2024)
        True
        >>> calcular_any_traspas(2023)
        False
    """
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)

def comptar_dies_mes(mes, any):
    """
    Retorna el nombre de dies d'un mes, tenint en compte si l'any és de traspàs.

    Args:
        mes (int): Número del mes (1-12)
        any (int): Any corresponent

    Returns:
        int: Dies del mes o missatge d'error si el mes és invàlid

    Examples:
        >>> comptar_dies_mes(2, 2020)
        29
        >>> comptar_dies_mes(2, 2023)
        28
        >>> comptar_dies_mes(4, 2023)
        30
        >>> comptar_dies_mes(13, 2023)
        'Mes invàlid'
    """
    dies_mes = {
        1: 31,
        2: 29 if calcular_any_traspas(any) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return dies_mes.get(mes, "Mes invàlid")

def comprovar_num_perfecte(num):
    """
    Comprova si un número és perfecte.

    Args:
        num (int): Número enter positiu

    Returns:
        bool: True si és perfecte, False si no ho és

    Examples:
        >>> comprovar_num_perfecte(6)
        True
        >>> comprovar_num_perfecte(28)
        True
        >>> comprovar_num_perfecte(10)
        False
    """
    if num <= 0:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def sumar(a, b):
    """
    Retorna la suma de dos nombres.

    Args:
        a (int): Primer nombre
        b (int): Segon nombre

    Returns:
        int: Resultat de la suma

    Examples:
        >>> sumar(12, 5)
        17
        >>> sumar(-3, 10)
        7
    """
    return a + b

def resta(a, b):
    """
    Retorna la resta de dos nombres.

    Args:
        a (int): Primer nombre
        b (int): Segon nombre

    Returns:
        int: Resultat de la resta

    Examples:
        >>> resta(10, 3)
        7
        >>> resta(5, 9)
        -4
    """
    return a - b

def multiplica(a, b):
    """
    Retorna el producte de dos nombres.

    Args:
        a (int): Primer nombre
        b (int): Segon nombre

    Returns:
        int: Resultat del producte

    Examples:
        >>> multiplica(3, 4)
        12
        >>> multiplica(-2, 6)
        -12
    """
    return a * b

def divideix(a, b):
    """
    Retorna la divisió entre dos nombres.

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        float or str: Resultat de la divisió o error si el divisor és 0

    Examples:
        >>> divideix(10, 2)
        5.0
        >>> divideix(7, 0)
        'No es pot dividir per zero'
    """
    if b == 0:
        return "No es pot dividir per zero"
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Executat doctest. Veure resultats a la consola si hi ha errors.")

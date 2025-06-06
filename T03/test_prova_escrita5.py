# test_prova_escrita5.py

import pytest
from prova_escrita5 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

# 📚 Base de dades d'exemple per a totes les proves
biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Anna", "dies": 25, "retornat": True},
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 10, "retornat": True}
        ]
    }
]

@pytest.mark.parametrize("categoria, resultat_esperat", [
    ("novel·la", ["El Quixot", "Crim i Càstig"]),
    ("ciència-ficció", ["1984"]),
    ("fantasia", []),
])
def test_llibres_per_categoria(categoria, resultat_esperat):
    """
    Test per la funció llibres_per_categoria.
    Comprova que retorni correctament els llibres segons la categoria indicada.
    """
    assert llibres_per_categoria(biblioteca, categoria) == resultat_esperat


@pytest.mark.parametrize("titol, resultat_esperat", [
    ("El Quixot", False),       # Té un préstec no retornat
    ("1984", True),             # Tots retornats
    ("Crim i Càstig", True),    # Tots retornats
    ("Inexistent", True),       # No hi és = es considera disponible
])
def test_esta_disponible(titol, resultat_esperat):
    """
    Test per la funció esta_disponible.
    Comprova si un llibre està disponible (tots els préstecs han estat retornats).
    """
    assert esta_disponible(biblioteca, titol) == resultat_esperat


@pytest.mark.parametrize("usuari, resultat_esperat", [
    ("Maria", True),    # Té un llibre no retornat
    ("Joan", False),    # Tots retornats
    ("Anna", False),    # Tots retornats
    ("Pere", False),    # No té préstecs en aquesta base
])
def test_usuari_te_prestecs(usuari, resultat_esperat):
    """
    Test per la funció usuari_te_prestecs.
    Comprova si un usuari té llibres pendents de retornar.
    """
    assert usuari_te_prestecs(biblioteca, usuari) == resultat_esperat


@pytest.mark.parametrize("titol, resultat_esperat", [
    ("El Quixot", 35),         # 15 + 20
    ("1984", 25),              # 25
    ("Crim i Càstig", 10),     # 10
    ("Inexistent", 0),         # No existeix
])
def test_dies_prestec_total(titol, resultat_esperat):
    """
    Test per la funció dies_prestec_total.
    Comprova la suma total de dies de préstec d’un llibre.
    """
    assert dies_prestec_total(biblioteca, titol) == resultat_esperat

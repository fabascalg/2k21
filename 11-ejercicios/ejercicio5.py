"""
    Ejercicio 5.

    Tabla a crear:

    ACCION       AVENTURA            DEPORTES
      GTA     ASSINS                  FIFA 21
      COD     CRASH                   PRO 21
      PUGB    Prince of Persia        MOTO GP 21

"""

tabla = [
    {
        "genero": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "genero": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "Prince of Persia"]
    },
    {
        "genero": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for genero in tabla:
    print(f"Género: {genero['genero']}")
    n = 1
    for campo in genero['juegos']:
        print(f"Juego {n}: {campo}")
        n += 1
    print("---------------------------------")

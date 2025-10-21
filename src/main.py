import BuscaMinas


def main():
    tablero = BuscaMinas.BuscaMinas(10, 10, 10)
    minas = tablero.minas(tablero.tablero, tablero.num_minas)
    print(f"Minas colocadas: {minas}")
    print("Tablero con minas:")
    for fila in tablero.tablero:
        print(fila)


if __name__ == "__main__":
    main()
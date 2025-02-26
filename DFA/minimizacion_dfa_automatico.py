import sys

def find_equivalent_pairs(n, final_states, transitions):
    # Creamos una tabla para marcar pares diferenciados (solo para i < j)
    marked = [[False] * n for _ in range(n)]
    
    # Inicialmente se marcan los pares donde uno es final y el otro no lo es.
    for i in range(n):
        for j in range(i + 1, n):
            if ((i in final_states) != (j in final_states)):
                marked[i][j] = True

    # Propagamos las diferencias:
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not marked[i][j]:
                    # Revisamos para cada símbolo si la transición lleva a un par ya marcado.
                    for symbol_index in range(len(transitions[0])):
                        ti = transitions[i][symbol_index]
                        tj = transitions[j][symbol_index]
                        # Aseguramos el orden para consultar en la tabla (menor primero)
                        a, b = (ti, tj) if ti < tj else (tj, ti)
                        if marked[a][b]:
                            marked[i][j] = True
                            changed = True
                            break

    # Los pares no marcados son equivalentes.
    eq_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not marked[i][j]:
                eq_pairs.append((i, j))
    return eq_pairs

def main():
    # Se lee el archivo "input.txt"
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    index = 0
    # Primer línea: cantidad de casos.
    cases = int(lines[index])
    index += 1

    # Para cada caso se procesa la entrada y se calcula el resultado.
    for _ in range(cases):
        n = int(lines[index])
        index += 1

        # El alfabeto se lee (aunque en este algoritmo se usa solo para determinar
        # la cantidad de columnas en la tabla de transición).
        alphabet = lines[index].split()
        index += 1

        # Se leen los estados finales (convertidos a enteros).
        final_states = set(map(int, lines[index].split()))
        index += 1

        # Se leen n líneas de la tabla de transición.
        transitions = []
        for i in range(n):
            row = list(map(int, lines[index].split()))
            index += 1
            transitions.append(row)

        # Se obtienen los pares de estados equivalentes.
        eq_pairs = find_equivalent_pairs(n, final_states, transitions)

        # Se formatea la salida: cada par se imprime como (i,j) y todos los pares en una línea.
        result = " ".join("({},{})".format(p, q) for p, q in eq_pairs)
        print(result)

if __name__ == "__main__":
    main()

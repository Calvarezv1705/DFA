# DFA
## 1. Información de los Estudiantes del equipo
- **Nombre del estudiante:** Camilo ALvarez Villegas, Sara Echeverri
- **Número de clase:** Camilo ALvarez VIllegas(Lunes de 6pm-9pm 7308), Sara Echeverri(Miercoles de 6pm-9pm)

## 2. Versiones del Sistema Operativo, Lenguaje de Programación y Herramientas
- **Sistema Operativo:** Windows 10 (64-bit) 
- **Lenguaje de Programación:** Python 3.9.7 
- **Herramientas y Librerías Utilizadas:**
  - Biblioteca sys

## 3. Instrucciones para Ejecutar la Implementación
1. **Descargar o clonar** 
2. Asegurarse de tener **Python 3** instalado y disponible en la terminal.
3. Ubicar el archivo **`input.txt`** en la misma carpeta donde está el código `minimiza_dfa.py`.
4. Abrir una terminal en la carpeta donde se encuentra el archivo.
5. Ejecutar el script con el siguiente comando:
   ```bash
   python minimiza_dfa.py
   ```
   o instalar la extencion code runner y ejecutar normalmente el codigo
  
6. El programa leerá el archivo **`input.txt`** y mostrará los resultados en la consola.

### Formato del Archivo `input.txt`
El archivo de entrada debe seguir el siguiente formato:
1. La primera línea contiene un número entero, que indica la cantidad de casos de prueba.
2. Para cada caso de prueba:
   - Una línea con un número entero, que representa la cantidad de estados.
   - Una línea con los símbolos del alfabeto (separados por espacios).
   - Una línea con los estados finales (separados por espacios).
   - `n` líneas, cada una con las transiciones de un estado (una fila por estado, con una columna por cada símbolo del alfabeto).

## 4. Explicación del Algoritmo
Este programa implementa el **algoritmo de minimización de DFA**. A continuación, se explica su funcionamiento:

1. **Marcar pares de estados distinguibles (Paso Inicial)**
   - Se marcan como diferentes aquellos pares `(p, q)` donde uno es un estado final y el otro no lo es.

2. **Propagar diferencias**
   - Si un par `(p, q)` no está marcado, pero al hacer una transición con algún símbolo llevan a un par `(r, s)` ya marcado, entonces `(p, q)` también se marca.

3. **Repetir hasta estabilidad**
   - Este proceso se repite hasta que en una iteración completa no haya más cambios en la tabla de marcados.

4. **Determinar los estados equivalentes**
   - Los pares de estados que no han sido marcados son equivalentes y pueden ser fusionados en el DFA minimizado.

El programa imprime los pares de estados equivalentes.


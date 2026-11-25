UD01 · Python básico
Bloque A · Entrada, tipos y operadores
1. Pide al usuario su nombre y su edad, y muestra una frase del estilo "Ana tendrá 23 años el año que viene". Pista: input, int, f-string.
2. Dados dos números enteros, muestra su división normal, su división entera, el resto y la potencia del primero elevado al segundo. Pista: /, //, %, **.
3. Comprueba, sin ejecutar, qué crees que devuelve 0.1 + 0.2 == 0.3 y después verifícalo. Explica con tus palabras por qué. Pista: punto flotante.
4. Dado un texto cualquiera, muéstralo en mayúsculas, sin espacios al inicio y al final, y con la letra "a" sustituida por "@". Pista: .upper(), .strip(), .replace().
5. Escribe una expresión que diga si un número x está entre 10 y 20 (ambos incluidos) usando una comparación encadenada. Pista: a <= x <= b.
Bloque B · Colecciones
6. Crea una lista con 6 números. Muéstrala invertida, muestra solo los dos primeros y solo los dos últimos. Pista: slicing.
7. Dada una lista con números repetidos, obtén otra lista sin duplicados. Pista: set, list.
8. Crea un diccionario con tres productos y sus precios. Pide un nombre y muestra su precio, o "No existe" si no está, sin que el programa falle. Pista: .get().
9. Dados dos conjuntos de alumnos (uno de los que van a Inglés, otro de los que van a Francés), muestra quiénes van a ambas, a alguna de las dos y solo a Inglés. Pista: &, |, -.
10. Intercambia el valor de dos variables sin usar una tercera, y desempaqueta una tupla de tres elementos en tres variables. Pista: asignación múltiple.
Bloque C · Control de flujo
11. Pide una nota numérica y muestra "Suspenso", "Aprobado", "Notable" o "Sobresaliente" según el tramo. Pista: if / elif / else.
12. Muestra la tabla de multiplicar de un número pedido al usuario, del 1 al 10. Pista: for, range.
13. Recorre una lista de ciudades mostrando posición y nombre (empezando en 1). Pista: enumerate.
14. Haz un programa que pida números hasta que el usuario escriba "fin" y al final muestre la suma. Pista: while True, break.
15. Pide dos números y divide el primero entre el segundo, controlando que no sea un texto ni un cero, y mostrando siempre "Operación terminada" al final. Pista: try / except / finally.
16. Crea un iterador a partir de una lista de 3 elementos y recupéralos a mano con next(). Después provoca el StopIteration. Pista: iter, next.
Bloque D · Funciones
17. Escribe una función area_rectangulo(base, altura=1) que devuelva el área (no que la imprima). Llámala de tres formas distintas. Pista: return, argumentos por nombre y por defecto.
18. Escribe una función que reciba un número variable de números y devuelva su media, controlando el caso sin argumentos. Pista: *args.
19. Escribe una función que reciba datos de una persona como argumentos con nombre y los muestre uno por línea. Pista: **kwargs, .items().
20. Dada una lista de números, obtén con una sola comprensión los cuadrados de los impares. Pista: comprensión con if.
21. Usa map con una lambda para convertir una lista de temperaturas de ºC a ºF, y filter para quedarte solo con las mayores de 80 ºF. Pista: list(map(...)), list(filter(...)).
22. Escribe una función crear_multiplicador(n) que devuelva otra función que multiplique por n. Crea doble y triple. Pista: clausura.
Bloque E · Clases, módulos y avanzado
23. Crea una clase Coche con marca y velocidad, un método acelerar(km) y un __str__ que muestre "Seat: 90 km/h". Pista: __init__, self, __str__.
24. Crea una clase Vehiculo y una subclase Moto que sobrescriba un método sonido(). Pista: herencia.
25. Añade a una clase un atributo de clase contador y un @classmethod que lo muestre; y un @staticmethod que compruebe si un número es par. Pista: cls, sin self.
26. Escribe un generador que produzca los números pares hasta un límite y recórrelo con un for. Pista: yield.
27. Escribe un decorador que muestre cuánto tarda en ejecutarse cualquier función, y aplícalo a una función que haga un bucle largo. Pista: time, functools.wraps, *args, **kwargs.
28. Crea un archivo con una función main() y protege su ejecución de forma que no corra si otro archivo lo importa. Pista: __name__.
29. Importa el módulo math de dos formas distintas y calcula una raíz cuadrada y un redondeo hacia arriba. Pista: import ... as, from ... import.
Mini proyecto UD01: gestor de tareas en consola (lista de diccionarios con nombre, prioridad y hecha; menú con while True; funciones para agregar, completar, ver y calcular el progreso sin dividir entre cero; rechaza nombres vacíos o repetidos).
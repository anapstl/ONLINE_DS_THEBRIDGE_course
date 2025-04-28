def cast_n_dia_a_dia_semana(n: int):
    """
    Convierte un número entero n en una cadena que representa el día de la semana correspondiente.
    
    :param n:  Número entero que representa el día de la semana (0-6)
    :return:  String que representa el día de la semana
    """

    dias = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
    return dias.get(n, 'Número inválido')

def piramide(n_filas):
    """
    Imprime una pirámide de números con n filas.
    """
    lst = list(range(1, n_filas + 1))
    lst.reverse()
    i = 0
    for elem in lst:
        lst_aux = lst[i:]
        i += 1
        for elem2 in lst_aux:
            print(elem2, end=" ")
        print()

def compara(primero, segundo):
    """
    Compara dos números y devuelve si son iguales, el primero es mayor o menor.
    """
    if primero < segundo:
        return "Segundo mayor que primero"
    elif primero == segundo:
        return "Son iguales"
    else:
        return "Primero mayor que segundo"

def contador_letras(texto, letra_a_contar):
    """
    Cuenta cuántas veces aparece una letra en un texto.
    """
    return texto.lower().count(letra_a_contar.lower())

def contador_generico(txt):
    """
    Cuenta cuántas veces aparece cada letra en un texto.
    """
    dict_result = {}
    for letra in txt:
        if letra.isalpha():
            dict_result[letra] = dict_result.get(letra, 0) + 1
    return dict_result

def ops_lista(lista, cmd, elemento=None):
    """
    Realiza operaciones en una lista según el comando dado.
    """
    if cmd == "add":
        lista.append(elemento)
    elif cmd == "remove":
        lista.remove(elemento)
    else:
        print("Comando no válido")
    return lista

def n_random_words(*args):
    """
    Genera una frase completa separando las n palabras aleatorias con espacios.
    """
    return " ".join(args)

def fibonacci(n):
    """
    Genera una lista con los primeros n números de la serie de Fibonacci.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calc_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado su lado.
    """
    return lado ** 2

def calc_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    """
    return (base * altura) / 2

def calc_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    """
    return 3.14 * (radio ** 2)
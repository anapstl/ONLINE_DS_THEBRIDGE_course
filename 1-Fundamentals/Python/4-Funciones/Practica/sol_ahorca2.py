palabra_adivinar = "python"
vidas = 10
palabra_oculta = ["_"] * len(palabra_adivinar)
letras_probadas = set()
error = 0

print("Bienvenido al juego de adivinar la palabra")
print("Tienes", vidas, "vidas para adivinar la palabra")
print("La palabra secreta es: ", " ".join(palabra_oculta))

letra = input("Introduce una letra para adivinar la palabra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, introduce solo una letra.")

if letra in letras_probadas:
    print("Ya has adivinado esa letra. Intenta con otra.")

while vidas > 0 and "_" in palabra_oculta:
    letras_probadas.add(letra)

    if letra in palabra_adivinar:
        print("¡Correcto! La letra está en la palabra.")
        for i, l in enumerate(palabra_adivinar):
            if l == letra:
                palabra_oculta[i] = letra
    else:
        error += 1
        vidas -= 1
        print("Incorrecto. Te quedan", vidas, "vidas.")

    if "_" not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra:", "".join(palabra_oculta))
        break

    print("Palabra actual:", " ".join(palabra_oculta))
    letra = input("Introduce otra letra: ").lower()
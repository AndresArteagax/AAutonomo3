import random

palabras = ["amor", "llover", "nostalgia", "facil", "desarrollador"]

palabra_secreta = random.choice(palabras)

progreso = ["_"] * len(palabra_secreta)  
intentos_restantes = 6  
letras_intentadas = []  

print("¡Bienvenido al juego del Ahorcado!")
print(f"La palabra tiene {len(palabra_secreta)} letras.")
print(" ".join(progreso))


while intentos_restantes > 0 and "_" in progreso:
    print(f"\nIntentos restantes: {intentos_restantes}")
    print(f"Letras intentadas: {', '.join(letras_intentadas)}")

   
    intento = input("Adivina una letra: ").lower()

    if len(intento) != 1 or not intento.isalpha():
        print("Por favor, introduce una sola letra.")
        continue
    if intento in letras_intentadas:
        print("Ya has intentado esa letra. Prueba con otra.")
        continue
       
        
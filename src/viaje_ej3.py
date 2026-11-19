edad = int(input("¿Qué edad tienes?"))
nivel_fisico = int(input("¿Cuál sería tu nivel físico en una escala de 1 a 10?"))
if edad > 18:
    if nivel_fisico < 5:
        print("Debes estar en mejor forma.")
    else:
        print("¡Listo para despegar!")
else:
    print("Debes ser mayor de edad.")
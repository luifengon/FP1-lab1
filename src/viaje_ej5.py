res = "s"
while res == "s":
    distancia_km =  int(input("¿Qué distancia vas a recorrer en km?"))
    velocidad_kmh = int(input("¿A qué velocidad vas a recorrer esa distancia en km/h?"))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    res = input("¿Quieres hacer otra simulación? (s/n)")
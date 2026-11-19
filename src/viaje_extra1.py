distancia_total = int(input("¿Qué distancia vas a recorrer en km?"))
distancia_parada = 150000
paradas_totales = 0
print(f"Introduce la distancia total en km: {distancia_total}")
for i in range(150000, distancia_total, distancia_parada):
    print(f"Parada en el km {i}")
    paradas_totales += 1
print(f"Total de paradas para repostar: {paradas_totales}")
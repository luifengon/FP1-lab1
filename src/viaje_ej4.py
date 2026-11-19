distancia_km = 225000000
velocidad_kmh = 0
for velocidad_kmh in range(10000, 60000, 10000):
    tiempo_dias = (distancia_km / velocidad_kmh)/24
    print(f"Velocidad: {velocidad_kmh} km/h -> Tiempo: {tiempo_dias} días")
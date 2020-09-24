Objetivo = int(input("Escoge un número: "))
Epsilon = 0.001
Bajo = 0.0
Alto = max(1.0, Objetivo)
Respuesta = (Alto + Bajo)/2

while abs(Respuesta**2 - Objetivo) >= Epsilon:
    print(f"Bajo = {Bajo}, Alto = {Alto}, Respuesta = {Respuesta}")
    if Respuesta**2 < Objetivo:
        Bajo = Respuesta
    else:
        Alto = Respuesta
    
    Respuesta = (Alto + Bajo)/2

print(f"La raíz cuadrada de {Objetivo} es {Respuesta}")

import random

class Vehiculo:
    def __init__(self, posicion, velocidad):
        self.posicion = posicion
        self.velocidad = velocidad

    def mover(self):
        self.posicion += self.velocidad

class Semaforo:
    def __init__(self, posicion):
        self.posicion = posicion
        self.color = "rojo"

    def cambiar_color(self):
        self.color = "verde" if self.color == "rojo" else "rojo"

class Simuladortrafico:
    def __init__(self, largo, num_carros, semaforos):
        self.largo = largo
        self.num_carros = num_carros
        self.semaforos = semaforos
        self.Vehiculos = []
        for i in range(num_carros):
            posicion = random.randint(0, largo)
            velocidad = random.randint(1, 5)
            self.Vehiculos.append(Vehiculo(posicion, velocidad))

    def paso(self):
        for Vehiculo in self.Vehiculos:
            Vehiculo.mover()
            for semaforo in self.semaforos:
                if Vehiculo.posicion == semaforo.posicion and semaforo.color == "rojo":
                    Vehiculo.velocidad = 0
                elif Vehiculo.posicion == semaforo.posicion and semaforo.color == "verde":
                    Vehiculo.velocidad = random.randint(1, 5)
        for semaforo in self.semaforos:
            semaforo.cambiar_color()

    def run(self, pasos):
        for i in range(pasos):
            self.paso()
            print(self)

    def __str__(self):
        carretera = ["."] * self.largo
        for Vehiculo in self.Vehiculos:
            if Vehiculo.posicion >= self.largo:
                continue
            if carretera[Vehiculo.posicion] == ".":
                carretera[Vehiculo.posicion] = "🚗"
            else:
                carretera[Vehiculo.posicion] += "🚗"
        for semaforo in self.semaforos:
            if carretera[semaforo.posicion] == ".":
                carretera[semaforo.posicion] = "🔴" if semaforo.color == "rojo" else "🟢"
            else:
                carretera[semaforo.posicion] += "🔴" if semaforo.color == "rojo" else "🟢"
        return "".join(carretera)

semaforos = [Semaforo(10), Semaforo(20)]
simulador = Simuladortrafico(50, 10, semaforos)
simulador.run(20)

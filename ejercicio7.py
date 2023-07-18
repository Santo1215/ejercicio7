import random

class Vehiculo:
    def __init__(self, posicion, velocidad):
        self.posicion = posicion
        self.velocidad = velocidad

    def move(self):
        self.posicion += self.velocidad

class TrafficLight:
    def __init__(self, posicion):
        self.posicion = posicion
        self.color = "rojo"

    def change_color(self):
        self.color = "verde" if self.color == "rojo" else "rojo"

class TrafficSimulator:
    def __init__(self, largo, n_cars, traffic_lights):
        self.largo = largo
        self.n_cars = n_cars
        self.traffic_lights = traffic_lights
        self.Vehiculos = []
        for i in range(n_cars):
            posicion = random.randint(0, largo)
            velocidad = random.randint(1, 5)
            self.Vehiculos.append(Vehiculo(posicion, velocidad))

    def step(self):
        for Vehiculo in self.Vehiculos:
            Vehiculo.move()
            for traffic_light in self.traffic_lights:
                if Vehiculo.posicion == traffic_light.posicion and traffic_light.color == "rojo":
                    Vehiculo.velocidad = 0
                elif Vehiculo.posicion == traffic_light.posicion and traffic_light.color == "verde":
                    Vehiculo.velocidad = random.randint(1, 5)
        for traffic_light in self.traffic_lights:
            traffic_light.change_color()

    def run(self, steps):
        for i in range(steps):
            self.step()
            print(self)

    def __str__(self):
        road = ["."] * self.largo
        for Vehiculo in self.Vehiculos:
            if Vehiculo.posicion >= self.largo:
                continue
            if road[Vehiculo.posicion] == ".":
                road[Vehiculo.posicion] = "🚗"
            else:
                road[Vehiculo.posicion] += "🚗"
        for traffic_light in self.traffic_lights:
            if road[traffic_light.posicion] == ".":
                road[traffic_light.posicion] = "🔴" if traffic_light.color == "rojo" else "🟢"
            else:
                road[traffic_light.posicion] += "🔴" if traffic_light.color == "rojo" else "🟢"
        return "".join(road)

# Ejemplo de uso
traffic_lights = [TrafficLight(10), TrafficLight(20)]
simulator = TrafficSimulator(50, 10, traffic_lights)
simulator.run(20)
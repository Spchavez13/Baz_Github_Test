
class Car:
    def __init__(self, modelo,marca,anio) -> None:
        self.modelo = modelo
        self.marca = marca
        self.anio = anio

    def enceder_motor(self):
        print ("Este motor esta encendido")
               
    def apagar_motor (self):
        print ("este motor esta apagado")

class Electrico(Car):
        def cargando_bateria(self):
            print ("este auto esta cargando beteria")

class Hibrido (Car):
        def motor_hibrido(self):
            print ("Este motor funciona con gasolina o bateria")

carro_01 = Electrico( 'Prius', 'toyota',2023)

#atributos
print (carro_01.modelo)
print (carro_01.marca)
print (carro_01.anio)

#metodos
carro_01.enceder_motor()
carro_01.apagar_motor()
carro_01.cargando_bateria()

# ejecicio

carro_02 = Hibrido ('testa', 'x23', 2022)
print (carro_02.modelo)
print (carro_02.marca)
print (carro_02.anio)

carro_02.enceder_motor()
carro_02.apagar_motor()
carro_02.motor_hibrido()




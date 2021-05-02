import random
import Paquete
from abc import ABCMeta, abstractmethod


class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        

class Cliente(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, **kwargs, ruc=0):
        super().__init__(**kwargs)
        self.ruc = ruc        
        self.identificador = random.randint(0, 9) + super().ci

class Empleado(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def registrar_cliente(nombre, apellido, ci, ruc):
        cliente = Cliente(**kwargs)
        return cliente

    def registrar_paquete(codigo, descripcion, peso, fecha):
        paquete = Paquete(**kwargs)
        return paquete


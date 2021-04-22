# Eduardo Gomez
## Parcial 1 - Paradigmas de la programación


[![Parcial 1](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)



## Archivos

- Paquete.py 
- Transporte.py
- Empresa.py
- datos.py
- main.py

## Ejecutar
Descomprimir
```sh
unzip parcial1.zip
cd parcial1
```

Para Debian o Ubuntu:
```sh
python3 main.py
```
Otras distribuciones:
```sh
python main.py 
```


> El sistema generará de manera automática 
> el ticket de embarco con los obejetos de la 
> la clase Paquete instanciados en el archivo
> datos.py

El archivo datos.py se compone de un arreglo que contiene una simulación del proceso de recepcion de paquetes y su respectiva clasificación.Así también contiene los transportes disponibles. Esto fue realizado para proporcionar datos al sistema y eliminar la elaboración de interfaces no necesarias en esta entrega. 

## Pruebas
Puede modificar los datos que reciben las siguientes funciones para testear el comportamiento del sistema:

| Metodo | Parametros |
| ------ | ------ |
| asignar_embarque() | (Paquetes[], Transporte) |
| consultar_embarque() | (Transporte) |

- Transporte: se encuentra limitado a solo dos tipos (Aereo, Maritimo)
- El sistema limita la cantidad de paquetes que se pueden asignar a un transporte en función a su capacidad de carga
- Si el paquete a transportar excede la capacidad de carga, se lanzará una excepcion notificando la imposbilidad de transporte
- Es posible instanciar transportes con capacidades de cargas personalizadas para realizar pruebas de robustez

Enlace al proyecto:
https://github.com/educardenas97/paradigmas/tree/master/parcial1

**Desarrollado en Python3**

   [dill]: <https://github.com/joemccann/dillinger>
   

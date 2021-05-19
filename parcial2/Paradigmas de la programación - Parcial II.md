# Paradigmas de la programación - Parcial II
## Eduardo Gómez



Esta aplicación fue contruida integramente con Python en su versión 3.7.9


# **Caracteristicas**

- Registro de paquetes
- Registro de clientes
- Registro de empleados
- Registro de transportes
- Asignación automática de paquetes a transportes
- Calculo de costo de transpor  



> Si bien el sistema se encuentra avanzado, se necesitan agregar
> funciones para volverlo completamente funcional.
> 


# **Organización**
## Core

El Core del sistema se encuenta modularizado de la siguiente manera:

- [Class] - Todas las clases que conforman el sistema
- [Controller] - La parte operativa o el controlador
- [Database] - Paquete que interactua con la base de datos

## View
Interfaz por linea de comandos, esta a su vez cuenta con divisiones según el módulo
del sistema. Alguno de ellos son:
- **Menu Principal:**
En este se encuentran las opciones descriptas a continuación. La utilización de
la interfaz consite en un selector numérico el cual permite ingresar a las opciones
desplegadas. 
- **Administración:**
-- Agregar Empleado: en este apartado se nos permite agregar un empleado a la empresa
-- Agregar Cliente: se solicitan los datos para el registro de un nuevo cliente. Los campos
nombre, apellido y ci, son obligatorios para el correcto registro.
- **Paquetería:**
-- Registrar Paquete: todos los campos solicitados son obligatorios, con excepción del valor de
articulo para los paquetes menores a 2Kg.  *El input debe ser en gramos.*
-- Paquetes en transito: muestra los paquetes que ya poseen un transportes y esperan su entrega a destino
-- Paquetes pendientes: se nos muestra la cantidad de paquetes pendientes de transportes
-- Paquetes entregados: lista los paquetes que ya fueron entregados. **Función pendiente de implementación*
- **Transportes:**
-- Registrar transportes:todos los campos solicitados son obligatorios a excepción de la 
fecha de llegada a destino. En caso de no introducirse una fecha se asumirá el tiempo habitual de demora.
-- Ver transportes disponibles: se muestra con todos los transportes disponibles.

## Controller
Este paquete se encarga de la interacción entre los objetos instanciados y la interfaz del sistema,
así también se encarga de gestionar las llamadas a la base de datos y la validación de los datos. Todas 
las funciones se encuentran en el fichero App.py

## Test

A modo de facilitar la correción se facilitaron algunos archivos para realizar test a la capa de control

| Fichero | Acción a realizar |
| ------ | ------ |
| App | Test de todas la funciones del sistema |
| Transporte | Prueba de los métodos de la clase Transporte |
| Ticket | Prueba el módulo responsable de la generación de tickets |



# Instalación

Debian 10 (buster):
```sh
python3 index.py
```

Otras distribuciones:

```sh
python index.py
```




   
   [Class]: <https://github.com/educardenas97/paradigmas/tree/master/parcial2/app/Core/Class>
   [Controller]:<https://github.com/educardenas97/paradigmas/tree/master/parcial2/app/Core/>
   [Database]: <https://github.com/educardenas97/paradigmas/tree/master/parcial2/app/Core/>

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TransporteMaritimo = exports.TransporteAereo = exports.Transporte = void 0;
class Transporte {
    constructor(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega) {
        this.lista_paquetes = [];
        this.nombre = nombre;
        this.fecha_salida = fecha_salida;
        this.tarifa = tarifa;
        this.limite_peso = limite_peso;
        this.tiempo_entrega = tiempo_entrega;
        this.lista_paquetes = [];
        this.peso_embarque = 0;
    }
    cargar_paquete(paquete) {
        if (this.limite_peso > this.peso_embarque + paquete.peso) {
            this.lista_paquetes.push(paquete);
            this.peso_embarque += paquete.peso;
            return true;
        }
        else {
            return false;
        }
    }
}
exports.Transporte = Transporte;
class TransporteAereo extends (Transporte) {
    constructor(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega) {
        super(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega);
    }
}
exports.TransporteAereo = TransporteAereo;
class TransporteMaritimo extends (Transporte) {
    constructor(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega) {
        super(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega);
    }
}
exports.TransporteMaritimo = TransporteMaritimo;

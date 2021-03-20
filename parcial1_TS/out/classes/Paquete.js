"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PaqueteGrande = exports.PaqueteMediano = exports.PaqueteChico = exports.Paquete = void 0;
class Paquete {
    constructor(nombre, peso, fecha_recepcion) {
        this.nombre = nombre;
        this.peso = peso;
        this.fecha_recepcion = fecha_recepcion;
    }
}
exports.Paquete = Paquete;
class PaqueteChico extends (Paquete) {
    constructor(nombre, peso, fecha_recepcion) {
        super(nombre, peso, fecha_recepcion);
    }
    calcular_costo(transporte) {
        return transporte.tarifa * this.peso;
    }
}
exports.PaqueteChico = PaqueteChico;
class PaqueteMediano extends (Paquete) {
    constructor(nombre, peso, fecha_recepcion) {
        super(nombre, peso, fecha_recepcion);
    }
    calcular_costo(transporte) {
        let total = transporte.tarifa * this.peso;
        return (total * 0.3) * 100;
    }
}
exports.PaqueteMediano = PaqueteMediano;
class PaqueteGrande extends (Paquete) {
    constructor(nombre, peso, fecha_recepcion) {
        super(nombre, peso, fecha_recepcion);
    }
    calcular_costo(transporte) {
        let total = transporte.tarifa * this.peso;
        return (total * 0.3) * 100;
    }
}
exports.PaqueteGrande = PaqueteGrande;

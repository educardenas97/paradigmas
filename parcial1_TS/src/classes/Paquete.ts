import { Transporte } from "./Transporte";

export abstract class Paquete{
    nombre: string;
    peso: number;
    fecha_recepcion: Date;

    constructor(nombre: string, peso: number, fecha_recepcion: Date) {
        this.nombre = nombre;
        this.peso = peso;
        this.fecha_recepcion = fecha_recepcion;
    }

    abstract calcular_costo(transporte: Transporte): number;
}


export class PaqueteChico extends(Paquete){
    constructor(nombre: string, peso: number, fecha_recepcion: Date){
        super(nombre, peso, fecha_recepcion);
    }

    calcular_costo(transporte: Transporte): number{
        return transporte.tarifa * this.peso;
    }
}


export class PaqueteMediano extends(Paquete){
    constructor(nombre: string, peso: number, fecha_recepcion: Date){
        super(nombre, peso, fecha_recepcion);
    }

    calcular_costo(transporte: Transporte): number{
        let total = transporte.tarifa * this.peso 
        return (total * 0.3) * 100;
    }
}


export class PaqueteGrande extends(Paquete){
    constructor(nombre: string, peso: number, fecha_recepcion: Date){
        super(nombre, peso, fecha_recepcion);
    }

    calcular_costo(transporte: Transporte): number{
        let total = transporte.tarifa * this.peso 
        return (total * 0.3) * 100;
    }
}

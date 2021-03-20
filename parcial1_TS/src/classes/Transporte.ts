import { Paquete } from "./Paquete";

export abstract class Transporte{
    nombre: string;
    fecha_salida: Date;
    tarifa: number;
    tiempo_entrega: number;
    limite_peso: number;
    peso_embarque: number;
    lista_paquetes: Paquete[] = [];
    

    constructor(nombre: string, fecha_salida: Date, tarifa: number, limite_peso: number, tiempo_entrega: number){
        this.nombre = nombre;
        this.fecha_salida = fecha_salida;
        this.tarifa = tarifa;
        this.limite_peso = limite_peso;
        this.tiempo_entrega = tiempo_entrega;
        this.lista_paquetes = [];
        this.peso_embarque = 0;
    }

    cargar_paquete(paquete: Paquete): boolean{
        if (this.limite_peso > this.peso_embarque + paquete.peso){
            this.lista_paquetes.push(paquete);
            this.peso_embarque += paquete.peso;
            return true;
        }else{
            return false;
        }
    }
}

export class TransporteAereo extends(Transporte){
    constructor(nombre: string, fecha_salida: Date, tarifa: number, limite_peso: number, tiempo_entrega: number){
        super(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega);
    }
}

export class TransporteMaritimo extends(Transporte){
    constructor(nombre: string, fecha_salida: Date, tarifa: number, limite_peso: number, tiempo_entrega: number){
        super(nombre, fecha_salida, tarifa, limite_peso, tiempo_entrega);
    }
}
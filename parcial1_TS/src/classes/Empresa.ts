import { Paquete } from "./Paquete";
import { Transporte } from "./Transporte";

export class Empresa{
    asignar_embarque(paquete: Paquete, transporte: Transporte): void{
        try {
            if (!transporte.cargar_paquete(paquete))
                throw new Error("Paquete no agregado");
        } catch (error) {
            console.error(error);
        }
    }

    consultar_embarque(transporte: Transporte): void{
        (transporte.lista_paquetes.forEach(paquete => {
            console.log( "Nombre: " + paquete.nombre + "Peso" + paquete.peso );
        }));
    }
}
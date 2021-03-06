"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Empresa = void 0;
class Empresa {
    asignar_embarque(paquete, transporte) {
        try {
            if (!transporte.cargar_paquete(paquete))
                throw (`Paquete no agregado: ${paquete.nombre} (${paquete.peso}Kg.)`);
        }
        catch (error) {
            console.error(error);
        }
    }
    consultar_embarque(transporte) {
        transporte.lista_paquetes.forEach((paquete) => {
            console.log(`Nombre: ${paquete.nombre} / Peso: ${paquete.peso}`);
        });
    }
}
exports.Empresa = Empresa;

import { Empresa } from "./classes/Empresa";
import { Paquete, PaqueteChico, PaqueteMediano, PaqueteGrande} from "./classes/Paquete";
import { Transporte, TransporteAereo } from "./classes/Transporte";

function crear_paquetes(): Paquete[] {
    return [new PaqueteChico("Noctua", 1, new Date("2015-03-25")), 
            new PaqueteChico("Redux", 2, new Date("2015-03-25")),
            new PaqueteGrande("Samsung", 78, new Date("2016-03-25"))];
}

function main() {
    let frontliner = new Empresa();
    let paquetes: Paquete[] = crear_paquetes();
    let avion: Transporte = new TransporteAereo("Carguero", new Date("2015-03-28"), 25, 400, 4);

    paquetes.forEach((paquete) => frontliner.asignar_embarque(paquete,avion));

    frontliner.consultar_embarque(avion)
}

main();
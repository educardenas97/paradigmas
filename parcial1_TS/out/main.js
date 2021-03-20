"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Empresa_1 = require("./classes/Empresa");
const Paquete_1 = require("./classes/Paquete");
const Transporte_1 = require("./classes/Transporte");
function crear_paquetes() {
    return [new Paquete_1.PaqueteChico("Noctua", 1, new Date("2015-03-25")),
        new Paquete_1.PaqueteChico("Redux", 2, new Date("2015-03-25")),
        new Paquete_1.PaqueteGrande("Samsung", 78, new Date("2016-03-25"))];
}
function main() {
    let frontliner = new Empresa_1.Empresa();
    let paquetes = crear_paquetes();
    let avion = new Transporte_1.TransporteAereo("Carguero", new Date("2015-03-28"), 25, 400, 4);
    paquetes.forEach((paquete) => frontliner.asignar_embarque(paquete, avion));
    frontliner.consultar_embarque(avion);
}
main();

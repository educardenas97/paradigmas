%EDUARDO GOMEZ 4659580

%Paquete a registrar en el sistema
%(Codigo, Descripcion, peso)
paquete('8081', teclado, 500).


%Regla que comprueba si el registro es correcto
es_registrable(Codigo, Peso):-paquete(Codigo,_,Peso), Peso>0.


%Estados posibles para el transporte
estado_transporte(disponible).
estado_transporte(transito).
estado_transporte(destino).

%Transporte registrado
%(Capacidad, Estado)
transporte(100,estado_transporte(disponible)).

%Regla para comprobar si es utilizable el transporte
es_utilizable(Capacidad, Estado):-transporte(Capacidad,Estado), Estado=disponible, Capacidad>0.

%Regla de comprobacion para el transporte del paquete
es_transportable(Peso, Capacidad):-paquete(_,_,Peso), transporte(Capacidad,_), Peso<Capacidad.
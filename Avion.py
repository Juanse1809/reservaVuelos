from Silla import Silla
class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []

        self.definicionSillasEjecutivas()
        self.definicionSillasEconomicas()

    def definicionSillasEjecutivas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.ventana  )
            else:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.pasillo  )

    def definicionSillasEconomicas(self):
        for i in range(self.SILLAS_ECONOMICAS):
            if (i+1)%3 == 0:
                self.sillasEconomicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.ventana)
            
            elif i+1 %3 == 1:
                self.sillasEconomicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.centro)
            
            else:
                self.sillasEconomicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.pasillo)



class Silla:

    CLASE = {
        "eje" : "Ejecutiva",
        "eco" : "economica"
    }

    UBICACION = {
        "ventana" : "Ventana",
        "centro" : "Centro",
        "pasillo" : "Pasillo"
    }
 
    def __init__(self, pNumero, pClase, pUbicacion):
        self.Numero = pNumero
        #operador ternario forma 1 - operador pClase debe ser true or false 
        self.Clase = (self.CLASE.eje, self.CLASE.eco)[pClase]
        # operador ternario forma 2
        # self.clase = self.CLASE.eje if pClase =="ejecutiva" else self.CLASE.eco
        if pUbicacion == "ventana":
            self.__ubicacion = self.UBICACION.ventana
        elif pUbicacion == "centro":
            self.__ubicacion = self.UBICACION.centro
        elif pUbicacion == "pasillo":
            self.__ubicacion = self.UBICACION.pasillo
        else:
            self.__ubicacion = None
        
        self.__pasajero = None

    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def designarPasajero(self):
        return True if self.__numero == None else False
            
    def getNumero(self):
        return self.__numero
    
    def getClase(self):
        return self.__clase
    
    def getUbicacion(self):
        return self.__ubicacion
    
    def getPasajero(self):
        return self.__pasajero
    
    




    #[]es un arreglo {} es objeto
    #ejem
    #persona = {
    #    "nombre" : "Daniel",
    #    "Apellido" : "Arteaga",
    #    "fNacimiento" : "1-1-2020"
    #}

    #persona.nombre
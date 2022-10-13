from itertools import groupby

def Vehiculos():
    class Vehiculos: # Clase Vehiculos
        def __init__(self, Barco, Tren, Avion, Camion):
            self.Primer_Transporte = Barco
            self.Segundo_Transporte = Tren
            self.Tercer_Transporte = Avion
            self.Cuarto_Transporte = Camion
             
        def cantidad_de_cada_transporte(self):
            print(self.Primer_Transporte, self.Segundo_Transporte, self.Tercer_Transporte, self.Cuarto_Transporte)
        
    
    class Barco(Vehiculos): #Clase Vehiculo
        pass
    print("TIPOS DE VEHICULOS DISPONIBLES ")
    print("################################################\n")
    B = Barco(1000, 100, 10,5)#Barco|Tren|Avion|Camion
    print("hay una cantidad total de Barcos Disponibles de {}\n".format(1000))
    
    
    class Tren(Vehiculos):  # Clase Asignada para el vehiculo Tren
        pass
    T = Tren(1000, 100, 10,5)#Barco|Tren|Avion|Camion
    print("hay una cantidad total de Tren Disponibles de {}\n".format(100))
           
 
    
       
    class Avion(Vehiculos): # clase asignada para el vehiculo Avion
        pass
    B = Avion(1000, 100, 10,5)#Barco|Tren|Avion|Camion
    print("hay una cantidad total de Avion Disponibles de {}\n".format(10))
    

   
    class Camion(Vehiculos):  #clase asignada para el vehiculo camion
        pass
    B = Camion(1000, 100, 10,5)#Barco|Tren|Avion|Camion
    print("hay una cantidad total de Camion Disponibles de {}\n".format(5))
    print("################################################\n")

def contenedores (): # funcion creada para guardar las clases creadas para identificar los contenedores 
    class contenedores: # clase que divide los contenedores
        def __init__(self, Normal_Pequeno, Normal_Grande, Refrigerado_Pequeno, Refrigerado_Grande, Estanque_liquidos, Estanque_liquidos_inflamables):
            self.Primer_Contenedor = Normal_Pequeno
            self.Segundo_Contenedor = Normal_Grande
            self.Tercer_Contenedor = Refrigerado_Grande
            self.Cuarto_Contenedor = Refrigerado_Pequeno
            self.Quinto_Contenedor = Estanque_liquidos
            self.Sexto_Contenedor = Estanque_liquidos_inflamables
             
        def cantidad_de_cada_contenedor(self):
            print(self.Primer_Contenedor, self.Segundo_Contenedor, self.Tercer_Contenedor, self.Cuarto_Contenedor, self.Quinto_Contenedor, self.Sexto_Contenedor)
            
    class Normal_Pequeno(contenedores): # clase creada para el contenedor normal pequeno
            pass
    N_P = Normal_Pequeno(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("TIPOS DE CONTENEDORES Y SU DISPONIBILIDAD\n")
    print("Hay una cantidad total de contenedores normales pequenos disponibles de {}\n".format(12000))
        
    class Normal_Grande(contenedores): # clase creada por el contenedor normal y grande
        pass
    N_G = Normal_Grande(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("Hay una cantidad total de contenedores normales grandes  disponibles de {}\n".format(6000))
 
        
    class Refrigerado_Pequeno(contenedores): # clase creada por el contenedor refrigerado pequeno
        pass
    R_P = Refrigerado_Pequeno(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("Hay una cantidad total de contenedores refrigerados pequenos disponibles de {}\n".format(3000))
        
    class Refrigerado_Grande(contenedores):
        pass
    R_G = Refrigerado_Grande(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("Hay una cantidad total de contenedores Refrigerados Grandes disponibles de {}\n".format(1500))
    
    
    class Estanque_liquidos(contenedores):
        pass
    E_L = Estanque_liquidos(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("Hay una cantidad total de contenedores para guardar liquidos de {}\n".format(750))
    
    class Estanque_liquidos_inflamables(contenedores):
        pass
    E_L_I = Estanque_liquidos_inflamables(12000, 6000, 3000, 1500, 750, 375)#normal pequeno| Normal Grande| Refrigerado Pequeno| Refrigerado Grande| Estanque Liquido| Estanque liquidos Inflamables
    print("Hay una cantidad total de contenedores para guardar liquidos inflamables de {}\n".format(375))


def main ():
    Clase_V = Vehiculos()
    Clase_C = contenedores()

if __name__ == '__main__':
    main()
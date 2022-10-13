import csv 
from itertools import groupby
import pandas as pd 
from csv import DictReader
import pprint
import matplotlib.pyplot as plt
from tkinter import Tk
import tkinter
from tkinter import *
#Creacion del Programa Para la filtracion de Productos de la forma mas optimizada posible



def Vehiculos(): #Funcion de Vehiculos
    print("INFORMACION DE LOS VEHICULOS Y CONTENEDORES")
    print("##############################################\n")
    class Vehiculos: # Clase Vehiculos
        print("INFORMACION DE LA CAPACIDAD DE LOS VEHICULOS JUNTO CON SUS RESPECTIVOS VALORES ")
        print("------------------------------------------------------------------------------")
        class Barco: #Clase Vehiculo
            def __init__(self, costo_transporte_b, capacidad): # Definicion de los atributos de la clase 
                self.costo_transporte_b = costo_transporte_b # definicion del atributo costo_transporte_b
                self.capacidad = capacidad #definicion del atributo capacidad
            
            def imprime_p(a): #funcion que me imprime los valores del barco asignados 
                print("\n")
                print("BARCO") 
                print("--------------------------------------------------")
                print("Este es el costo de transporte de un Barco: {} ".format(a.costo_transporte_b))
                print("La capacidad de transporte es de {} contenedores estandar ".format(a.capacidad))
                
        b1 = Barco("$1.000.000.000", "24.000") # Valores de Barco
        b1.imprime_p() #Imprime los valores por pantalla 
    
        class Tren:  # Clase Asignada para el vehiculo Tren
            def __init__(self, costo_transporte_T, capacidad_t): # Funcion para asignar los atributos de la clase 
                self.costo_transporte_T = costo_transporte_T # tributo asignado para el costo de transporte 
                self.capacidad_t = capacidad_t # tributo asignado para la capacidad del transporte
            
            def imprime_p(b): # Funcion que imprime los valores por pantalla
                print("\n")
                print("TREN")
                print("--------------------------------------------------")
                print("Este es el costo de transporte de un Tren: {} ".format(b.costo_transporte_T))
                print("La capacidad de transporte es de {} contenedores estandar ".format(b.capacidad_t))

        t1 = Tren("$10.000.000", 250) # valores determinados de los contenedores 
        t1.imprime_p() 
    
       
        class Avion: # clase asignada para el vehiculo Avion
            def __init__(self, costo_transporte_A, capacidad_a): # Funcion creada para asignar los atributos del vehiculo Avion
                self.costo_transporte_A = costo_transporte_A # atributo para el costo del transporte
                self.capacidad_a = capacidad_a # atributo para la capacidad 
            
            def imprime_p(b): # Funcion para imprimir los valores por pantalla
                print("\n")
                print("AVION")
                print("------------------------------------------------")
                print("Este es el costo de transporte De un Avion: {} ".format(b.costo_transporte_A))
                print("La capacidad de transporte es de {} contenedores estandar ".format(b.capacidad_a))

        a1 = Avion("$1.000.000", 10)# valores predeterminados del costo del avion
        a1.imprime_p()
    
       
        class Camion:  #clase asignada para el vehiculo camion
            def __init__(self, costo_transporte_C, capacidad_c): # atributos asignados para el camion
                self.costo_transporte_C = costo_transporte_C # atributo para el costo del transporte
                self.capacidad_c = capacidad_c # atributo para la capacidad
            
            def imprime_p(b): # funcion asignada para imprimir  los valores por pantalla
                print("\n")
                print("CAMION")
                print("-----------------------------------")
                print("Este es el costo de transporte: {} ".format(b.costo_transporte_C))
                print("La capacidad de transporte es de {} contenedores estandar ".format(b.capacidad_c))

        c1 = Camion("$500", 1) # valores predeterminados por el costo del transporte 
        c1.imprime_p() 

def t_contenedores (): # funcion creada para guardar las clases creadas para identificar los contenedores 
    class contenedores: # clase que divide los contenedores
        print("\n")
        print("INFORMACION DE LOS CONTENEDORES Y SU CAPACIDAD DE TONELAJE")
        class Normal_Pequeno: # clase creada para el contenedor normal pequeno
            def __init__(self,carga_normal, carga_inerte, carga_solida): # define los valores de la clase
                self.carga_normal = carga_normal
                self.carga_inerte = carga_inerte
                self.carga_solida = carga_solida 
            
            def impresion_contenedores_N_P(a): # esta funcion imprime los valores
                print("\n")
                print("NORMALES/PEQUENOS")
                print("------------------")
                print("El Soporte de los contenedores Normales/Pequenos Para una Carga Normal es de {}".format(a.carga_normal))
                print("--------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Normales/Pequenos Para una Carga Inerte es de {}".format(a.carga_inerte))
                print("--------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Normales/Pequenos Para una Carga Solida es de {}".format(a.carga_solida))
        N_P= Normal_Pequeno(12, 12, 12) # define los valores de la clase del contenedor
        N_P.impresion_contenedores_N_P()

        class Normal_Grande: # clase creada por el contenedor normal y grande
            def __init__(self, carga_normal_g, carga_inerte_g, carga_solida_g): # define los valores de la clase
                self.carga_normal_g = carga_normal_g
                self.carga_inerte_g = carga_inerte_g
                self.carga_solida_g = carga_solida_g
                
            def impresion_contenedores_N_G(b): # imprime los valores por pantalla de los contenedores
                print("\n")
                print("NORMALES/GRANDES (ESTANDAR)(2 PEQUENOS)")
                print("----------------")
                print("El Soporte de los contenedores Normales/Grandes Para una Carga Normal es de {}".format(b.carga_normal_g))
                print("------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Normales/Grandes Para una Carga Inerte es de {}".format(b.carga_inerte_g))
                print("-------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Normales/Grandes Para una Carga Solida es de {}".format(b.carga_solida_g))
        N_G = Normal_Grande(24, 24, 24)
        N_G.impresion_contenedores_N_G()
        
        class Refrigerado_Pequeno: # clase creada por el contenedor refrigerado pequeno
            def __init__(self, carga_normal_n_p, carga_inerte_n_p, carga_solida_n_p, carga_refrigerada_n_p):
                self.carga_normal_n_p = carga_normal_n_p
                self.carga_refrigerada_n_p = carga_refrigerada_n_p
                self.carga_inerte_n_p = carga_inerte_n_p
                self.carga_solida_n_p = carga_solida_n_p
                
            def impresion_contenedores_R_P(c): # imprime los valores por pantalla
                print("\n")
                print("REFRIGERADO/PEQUENO")
                print("----------------")
                print("El Soporte de los contenedores Refrigerados Pequenos Para una Carga Normal es de {}".format(c.carga_normal_n_p))
                print("------------------------------------------------------------------------------------")                
                print("El Soporte de los contenedores Refrigerados Pequenos Para una Carga Refrigerada es de {}".format(c.carga_refrigerada_n_p))
                print("------------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Refrigerados Pequenos Para una Carga Inerte es de {}".format(c.carga_inerte_n_p))
                print("------------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Refrigerados Pequenos Para una Carga Solida es de {}".format(c.carga_solida_n_p))
                
        R_P= Refrigerado_Pequeno(10, 10, 10, 10) # define los valores de la clase del contenedor
        R_P.impresion_contenedores_R_P()
        
        class Refrigerado_Grande:
            
            def __init__(self, carga_normal_g_r, carga_inerte_g_r, carga_solida_g_r, carga_refrigerada_g_r):
                self.carga_normal_g_r = carga_normal_g_r
                self.carga_refrigerada_g_r = carga_refrigerada_g_r
                self.carga_inerte_g_r = carga_inerte_g_r
                self.carga_solida_g_r = carga_solida_g_r
                
            def impresion_contenedores_N_G(d):
                print("\n")
                print("REFRIGERADO/GRANDE (ESTANDAR)(2 PEQUENOS)")
                print("----------------")
                print("El Soporte de los contenedores Refrigerado Grande Para una Carga Normal es de {}".format(d.carga_normal_g_r))
                print("------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Refrigerado Grande Para una Carga Inerte es de {}".format(d.carga_inerte_g_r))
                print("-------------------------------------------------------------------------------")
                print("El Soporte de los contenedores Refrigerado Grande Para una Carga Solida es de {}".format(d.carga_solida_g_r))
                print("--------------------------------------------------------------------------------")
                print("EL Soporte de los contenedores Refrigerado Grande Para una Carga Refrigerada es de {}".format(d.carga_refrigerada_g_r))
                
        R_G = Refrigerado_Grande(20, 20, 20, 20)  # define los valores de la clase del contenedor
        R_G.impresion_contenedores_N_G()
        
    
    
    class Estanque_liquidos:
        
        def __init__(self, Carga_inerte_E, Carga_Liquida_E, Carga_gas_E):
            self.Carga_inerte_E = Carga_inerte_E
            self.Carga_Liquida_E = Carga_Liquida_E
            self.Carga_gas_E = Carga_gas_E
        
        def impresion_E_L(e):
                print("\n")
                print("ESTANQUES/LIQUIDOS (ESTANDAR)")
                print("----------------")
                print("El Soporte de los contenedores liquidos para una carga inerte es de  {}".format(e.Carga_inerte_E))
                print("------------------------------------------------------------------------------")
                print("El Soporte de los contenedores liquidos para una carga liquida es de {}".format(e.Carga_Liquida_E))
                print("-------------------------------------------------------------------------------")
                print("El Soporte de los contenedores liquidos para una carga de gas es de  {}".format(e.Carga_gas_E))
                print("--------------------------------------------------------------------------------") 
    E_L = Estanque_liquidos(24, 24, 24)  # define los valores de la clase del contenedor
    E_L.impresion_E_L()
    
    class Estanque_liquidos_inflamables:
        
        def __init__(self, Carga_inerte_E_L_I, Carga_inflamable_E_L_I, Carga_Liquida_E_L_I, Carga_gas_E_L_I):
            self.Carga_inerte_E_L_I = Carga_inerte_E_L_I
            self.Carga_inflamable_E_L_I = Carga_inflamable_E_L_I
            self.Carga_Liquida_E_L_I = Carga_Liquida_E_L_I
            self.Carga_gas_E_L_I = Carga_gas_E_L_I
             
        def impresion_E_L_I(f):
                print("\n")
                print("ESTANQUES LIQUIDOS INFLAMABLES (ESTANDAR)")
                print("----------------")
                print("El Soporte de los contenedores liquidos inflamables para una carga inerte es de  {}".format(f.Carga_gas_E_L_I))
                print("-----------------------------------------------------------------------------------")
                print("El Soporte de los contenedores liquidos inflamables para una carga liquida es de {}".format(f.Carga_Liquida_E_L_I))
                print("-----------------------------------------------------------------------------------")
                print("El Soporte de los contenedores liquidos inflamables para una carga de gas es de  {}".format(f.Carga_gas_E_L_I))
                print("-------------------------------------------------------------------------------------")
                print("El Soporte de los contenedores liquidos inflamables para una carga inflamable es de {}".format(f.Carga_inflamable_E_L_I)) 
    E_L_I = Estanque_liquidos_inflamables(20, 20, 20, 20)  # define los valores de la clase del contenedor
    E_L_I.impresion_E_L_I()
        
# ----------------------------------------------------------------        
        
def lectura_csv():  # funcion asigndad para el csv y filtrar los datos 
    with open('ejemplo_lista.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        #---------------------------------------------------------------
        print("\n")
        print("A CONTINUACION SE MUESTRA LA LISTA DE ARCHIVOS QUE SE FILTRARA")
        print("--------------------------------------------------------")
        for row in reader:
            print(row)
#-----------------------------------------------------------------------
# agrupacion de los productos dividida por vehiculos 

def distribucion_del_viaje_barco():
    
    class contenedores_barco_t:
        
        def __init__(self, Normal_Grande, Refrigerado_Grande, Estanque_liquidos, Estanque_liquidos_inflamables, total_contenedores):
            self.Normal_Grande = int(Normal_Grande) 
            self.Refrigerado_Grande = int(Refrigerado_Grande)
            self.Estanque_liquidos = int(Estanque_liquidos)
            self.Estanque_liquidos_inflamables = int(Estanque_liquidos_inflamables)
            self.total_contenedores = int(total_contenedores)
            
        def impresion_total_contenedores_b(a):
            print("#######################################")
            print("DISTRIBUCION DEL TONELAJE DEL BARCO\n")
            print("Cantidad de Contenedores Normales Grandes en el barco es {} \n".format(a.Normal_Grande))
            print("Cantidad de Contenedores Refrigerados Grandes en el barco es {} \n".format(a.Refrigerado_Grande))
            print("Cantidad de Contenedores Para Guardar liquidos en un barco es {} \n".format(a.Estanque_liquidos))
            print("Cantidad de Contenedores Para Guardar Liquidos inflamables en un barco es de {} \n".format(a.Estanque_liquidos_inflamables))
            print("Cantidad de Tonelaje Total = {}\n".format(a.total_contenedores))
           
        
    Barco_c = contenedores_barco_t(6000, 6000, 6000, 6000, 24000)
    B = {1, 1, 1, 1, 24000} # Datos para el histograma de la cantidad de contenedores distintos en el barco 
    Barco_c.impresion_total_contenedores_b()
    #---------------------------
    # Creacion del Histograma
    plt.hist(B, bins=10, color="blue", rwidth=0.9)
    plt.title("Cantidad de Contenedores Distintos")
    plt.xlabel("Cantidad")
    plt.ylabel("Cuantos Tipos hay de cada uno")
    plt.show()

def producto_barco():


    class productos_barco:
        
        def __init__(self, id_producto, nombre_producto, cantidad_del_producto , peso, cantidad_ocupada, tipo_contenedor, tipo_producto, masa):
            self.id_producto = int(id_producto)
            self.nombre_producto = nombre_producto
            self.peso = int(peso)
            self.cantidad_ocupada = int(cantidad_ocupada)
            self.tipo_contenedor = tipo_contenedor
            self.tipo_producto = tipo_producto
            self.masa = masa
            self.cantidad_ocupada = cantidad_ocupada
        print("#############################################################################")
        print("PRODUCTOS QUE TRANSPORTARA EL BARCO JUNTO CON SU RESPECTIVO CONTENEDOR \n ")
        
        def impresion_productos_que_se_transportan_en_barco_1(a):
            print("EL producto que se transportara en el barco es el siguiente:  {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(a.nombre_producto, a.tipo_contenedor, a.tipo_producto, a.masa, a.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_barco_2(b):   
            print("El producto que se transportara en el barco es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(b.nombre_producto, b.tipo_contenedor, b.tipo_producto, b.masa, b.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_barco_3(c):
            print("El producto que se transportara en el barco es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(c.nombre_producto, c.tipo_contenedor, c.tipo_producto, c.masa, c.masa))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_barco_4(d):    
            print("El producto que se transportara en el barco es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(d.nombre_producto, d.tipo_contenedor, d.tipo_producto, d.masa, d.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_barco_5(e):
            print("El producto que se transportara en el barco es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {}  \n".format(e.nombre_producto, e.tipo_contenedor,e.tipo_producto, e.masa, e.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
            
    producto_1 = productos_barco(1, "plancha_cobre", 10000, 10000, 14000, "Normal/Pequeno", "normal", "solida")
    producto_1.impresion_productos_que_se_transportan_en_barco_1()
    
    producto_2 = productos_barco(2, "carne_roja", 10000 , 10000, 13000, "Refrigerado/Pequeno", "refrigerado ", "solida")
    producto_2.impresion_productos_que_se_transportan_en_barco_2()
    
    producto_3 = productos_barco(4, "aceite_cocina", 3000 ,  3000, 10000, "Estanque_liquidos_inflamables", "inflamable", "liquido")
    producto_3.impresion_productos_que_se_transportan_en_barco_3()
    
    producto_4 = productos_barco(5, "verduras", 5000 , 5000, 5000, "Refrigerado/Grande", "refrigerado", "solida")
    producto_4.impresion_productos_que_se_transportan_en_barco_4()
    
    producto_5 = productos_barco(5, "verduras", 5000, 5000, 0, "Refrigerado/Grande", "refrigerado", "solida")
    producto_5.impresion_productos_que_se_transportan_en_barco_5()

    #---------------------------
    # Creacion del Histograma
    tonelaje_cada_producto = {10000, 1000, 3000, 5000, 5000} #producto1|producto2|producto3|producto4|producto5 
    
    plt.hist(tonelaje_cada_producto, bins=10, color="blue", rwidth=0.9)
    plt.title("tonelaje de cada producto")
    plt.xlabel("valores")
    plt.ylabel("tonelaje")
    plt.show()
    



def distribucion_del_viaje_tren():
    
    class contenedores_tren_t:
        
        def __init__(self,Pequeno_Normal, Normal_Grande, Refrigerado_Grande, Estanque_liquidos, Estanque_liquidos_inflamables, total_contenedores):
            self.Pequeno_Normal = Pequeno_Normal
            self.Normal_Grande = int(Normal_Grande) 
            self.Refrigerado_Grande = int(Refrigerado_Grande)
            self.Estanque_liquidos = int(Estanque_liquidos)
            self.Estanque_liquidos_inflamables = int(Estanque_liquidos_inflamables)
            self.total_contenedores = int(total_contenedores)
            
        def impresion_total_contenedores_t(a):
            print("#######################################")
            print("DISTRIBUCION DEL TONELAJE DEL TREN\n")
            print("Cantidad de Contenedores Normales Pequenos en el Tren es {} \n".format(a.Pequeno_Normal))
            print("Cantidad de Contenedores Normales Grandes en el Tren es {} \n".format(a.Normal_Grande))
            print("Cantidad de Contenedores Refrigerados Grandes en el Tren es {} \n".format(a.Refrigerado_Grande))
            print("Cantidad de Contenedores Para Guardar liquidos en un Tren es {} \n".format(a.Estanque_liquidos))
            print("Cantidad de Contenedores Para Guardar Liquidos inflamables en un Tren es de {} \n".format(a.Estanque_liquidos_inflamables))
            print("Cantidad de Tonelaje Total = {}\n".format(a.total_contenedores))
           
        
    Tren_c = contenedores_tren_t(50, 50, 50, 50, 50, 250)
    T = {1, 1, 1, 1, 1, 250} # Datos para el histograma de la cantidad de contenedores distintos en el Tren 
    Tren_c.impresion_total_contenedores_t()
    
    #---------------------------
    # Creacion del Histograma
    plt.hist(T, bins=10, color="red", rwidth=0.9)
    plt.title("Cantidad de Contenedores Distintos en el transporte del tren")
    plt.xlabel("Cantidad")
    plt.ylabel("Cuantos Tipos hay de cada uno")
    plt.show()
    
def producto_tren():
    
    class productos_tren:
        
        def __init__(self, id_producto, nombre_producto, cantidad_del_producto , peso, cantidad_ocupada, tipo_contenedor, tipo_producto, masa):
            self.id_producto = int(id_producto)
            self.nombre_producto = nombre_producto
            self.peso = int(peso)
            self.cantidad_ocupada = int(cantidad_ocupada)
            self.tipo_contenedor = tipo_contenedor
            self.tipo_producto = tipo_producto
            self.masa = masa
            self.cantidad_del_producto = cantidad_del_producto
        print("#############################################################################")
        print("PRODUCTOS QUE TRANSPORTARA EL TREN JUNTO CON SU RESPECTIVO CONTENEDOR \n ")
        
        def impresion_productos_que_se_transportan_en_tren_1(a):
            print("EL producto que se transportara en el tren es el siguiente:  {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(a.nombre_producto, a.tipo_contenedor, a.tipo_producto, a.masa, a.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_tren_2(b):   
            print("El producto que se transportara en el tren es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(b.nombre_producto, b.tipo_contenedor, b.tipo_producto, b.masa, b.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_tren_3(c):
            print("El producto que se transportara en el tren es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(c.nombre_producto, c.tipo_contenedor, c.tipo_producto, c.masa, c.masa))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_tren_4(d):    
            print("El producto que se transportara en el tren es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(d.nombre_producto, d.tipo_contenedor, d.tipo_producto, d.masa, d.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_tren_5(e):
            print("El producto que se transportara en el tren es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {}  \n".format(e.nombre_producto, e.tipo_contenedor,e.tipo_producto, e.masa, e.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
            
    producto_1_t = productos_tren(1, "plancha_cobre",50 ,10000, 200, "Normal_Pequeno", "normal", "solida")
    producto_1_t.impresion_productos_que_se_transportan_en_tren_1()
    
    producto_2_t = productos_tren(2, "carne_roja" ,50 ,1000, 150,  "Refrigerado_Pequeno", "refrigerado ", "solida")
    producto_2_t.impresion_productos_que_se_transportan_en_tren_2()
    
    producto_3_t = productos_tren(4, "aceite_cocina" ,50 , 3000, 100, "Estanque_liquidos_inflamables", "inflamable", "liquido")
    producto_3_t.impresion_productos_que_se_transportan_en_tren_3()
    
    producto_4_t = productos_tren(5, "carne_blanca" ,50 , 20000,  50, "Refrigerado_Grande", "refrigerado", "solida")
    producto_4_t.impresion_productos_que_se_transportan_en_tren_4()
    
    producto_5_t = productos_tren(5, "leche" ,50 ,15000, 0, "Refrigerado_Grande", "refrigerado", "liquida")
    producto_5_t.impresion_productos_que_se_transportan_en_tren_5()

    #---------------------------
    # Creacion del Histograma
                                
    tonelaje_cada_producto = {10000, 1000, 3000, 20000, 15000} #producto1|producto2|producto3|producto4|producto5
    
    plt.hist(tonelaje_cada_producto, bins=10, color="red", rwidth=0.9)
    plt.title("tonelaje de cada producto en el tren")
    plt.xlabel("valores")
    plt.ylabel("tonelaje")
    plt.show()

def distribucion_del_viaje_avion():
    
    class contenedores_avion_t:
        
        def __init__(self,Pequeno_Normal, Normal_Grande, Refrigerado_Grande, Estanque_liquidos, Estanque_liquidos_inflamables, total_contenedores):
            self.Pequeno_Normal = int(Pequeno_Normal)
            self.Normal_Grande = int(Normal_Grande) 
            self.Refrigerado_Grande = int(Refrigerado_Grande)
            self.Estanque_liquidos = int(Estanque_liquidos)
            self.Estanque_liquidos_inflamables = int(Estanque_liquidos_inflamables)
            self.total_contenedores = int(total_contenedores)
            
        def impresion_total_contenedores_a(a):
            print("#######################################")
            print("DISTRIBUCION DEL TONELAJE DEL AVION\n")
            print("Cantidad de Contenedores Normales Pequenos en el avion es {} \n".format(a.Pequeno_Normal))
            print("Cantidad de Contenedores Normales Grandes en el avion es {} \n".format(a.Normal_Grande))
            print("Cantidad de Contenedores Refrigerados Grandes en el avion es {} \n".format(a.Refrigerado_Grande))
            print("Cantidad de Contenedores Para Guardar liquidos en un avion es {} \n".format(a.Estanque_liquidos))
            print("Cantidad de Contenedores Para Guardar Liquidos inflamables en un avion es de {} \n".format(a.Estanque_liquidos_inflamables))
            print("Cantidad de Tonelaje Total = {}\n".format(a.total_contenedores))
           
        
    Avion_c = contenedores_avion_t(2, 2, 2, 2, 2, 10)
    A = {1, 1, 1, 1, 1, 10} # Datos para el histograma de la cantidad de contenedores distintos en el Avion
    Avion_c.impresion_total_contenedores_a()
    
    #---------------------------
    # Creacion del Histograma
    
    plt.hist(A, bins=10, color="green", rwidth=0.9)
    plt.title("Cantidad de Contenedores Distintos en el transporte del avion")
    plt.xlabel("Cantidad")
    plt.ylabel("Cuantos Tipos hay de cada uno")
    plt.show()
    
def producto_avion():
    
    class productos_avion:
        
        def __init__(self, id_producto, nombre_producto, cantidad_del_producto , peso, cantidad_ocupada, tipo_contenedor, tipo_producto, masa):
            self.id_producto = int(id_producto)
            self.nombre_producto = nombre_producto
            self.peso = int(peso)
            self.cantidad_ocupada = int(cantidad_ocupada)
            self.tipo_contenedor = tipo_contenedor
            self.tipo_producto = tipo_producto
            self.masa = masa
            self.cantidad_del_producto = cantidad_del_producto
        print("#############################################################################")
        print("PRODUCTOS QUE TRANSPORTARA EL AVION JUNTO CON SU RESPECTIVO CONTENEDOR \n ")
        
        def impresion_productos_que_se_transportan_en_avion_1(a):
            print("EL producto que se transportara en el avion es el siguiente:  {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(a.nombre_producto, a.tipo_contenedor, a.tipo_producto, a.masa, a.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_avion_2(b):   
            print("El producto que se transportara en el avion es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(b.nombre_producto, b.tipo_contenedor, b.tipo_producto, b.masa, b.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_avion_3(c):
            print("El producto que se transportara en el avion es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(c.nombre_producto, c.tipo_contenedor, c.tipo_producto, c.masa, c.masa))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_avion_4(d):    
            print("El producto que se transportara en el avion es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(d.nombre_producto, d.tipo_contenedor, d.tipo_producto, d.masa, d.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
        def impresion_productos_que_se_transportan_en_avion_5(e):
            print("El producto que se transportara en el avion es el siguiente: {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {}  \n".format(e.nombre_producto, e.tipo_contenedor,e.tipo_producto, e.masa, e.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
            
    producto_1_t = productos_avion(1, "plancha_cobre",2 ,10000, 8, "Normal_Pequeno", "normal", "solida")
    producto_1_t.impresion_productos_que_se_transportan_en_avion_1()
    
    producto_2_t = productos_avion(2, "carne_roja" ,2 ,1000, 6,  "Refrigerado_Pequeno", "refrigerado ", "solida")
    producto_2_t.impresion_productos_que_se_transportan_en_avion_2()
    
    producto_3_t = productos_avion(4, "aceite_cocina" ,2 , 3000, 4, "Estanque_liquidos_inflamables", "inflamable", "gas")
    producto_3_t.impresion_productos_que_se_transportan_en_avion_3()
    
    producto_4_t = productos_avion(5, "carne_blanca" ,2 , 20000,  2, "Refrigerado_Grande", "refrigerado", "solida")
    producto_4_t.impresion_productos_que_se_transportan_en_avion_4()
    
    producto_5_t = productos_avion(5, "leche" ,2 ,15000, 0, "Refrigerado_Grande", "refrigerado", "liquida")
    producto_5_t.impresion_productos_que_se_transportan_en_avion_5()

    #---------------------------
    # Creacion del Histograma                            
    tonelaje_cada_producto = {10000, 1000, 3000, 20000, 15000} #producto1|producto2|producto3|producto4|producto5
    
    plt.hist(tonelaje_cada_producto, bins=10, color="green", rwidth=0.9)
    plt.title("tonelaje de cada producto en el avion")
    plt.xlabel("valores")
    plt.ylabel("tonelaje")
    plt.show()

def distribucion_del_viaje_camion():
    
    class contenedores_camion_t:
        
        def __init__(self, Normal_Grande, total_contenedores):
            self.Normal_Grande = int(Normal_Grande) 
            self.total_contenedores = int(total_contenedores)
            
        def impresion_total_contenedores_c(a):
            print("#######################################")
            print("DISTRIBUCION DEL TONELAJE DEL CAMION\n")
            print("Cantidad de Contenedores Normales Grandes en el avion es {} \n".format(a.Normal_Grande))
            print("Cantidad de Tonelaje Total = {}\n".format(a.total_contenedores))
           
        
    camion_c = contenedores_camion_t(1, 1)
    C = {1, 1} # Datos para el histograma de la cantidad de contenedores distintos en el Camion
    camion_c.impresion_total_contenedores_c()
    
    #---------------------------
    # Creacion del Histograma

    plt.hist(C, bins=10, color="black", rwidth=0.9)
    plt.title("Cantidad de Contenedores Distintos en el transporte del camion")
    plt.xlabel("Cantidad")
    plt.ylabel("Cuantos Tipos hay de cada uno")
    plt.show()

    
def producto_camion():
    
    class productos_camion:
        
        def __init__(self, id_producto, nombre_producto, cantidad_del_producto , peso, cantidad_ocupada, tipo_contenedor, tipo_producto, masa):
            self.id_producto = int(id_producto)
            self.nombre_producto = nombre_producto
            self.peso = int(peso)
            self.cantidad_ocupada = int(cantidad_ocupada)
            self.tipo_contenedor = tipo_contenedor
            self.tipo_producto = tipo_producto
            self.masa = masa
            self.cantidad_del_producto = cantidad_del_producto
        print("#############################################################################")
        print("PRODUCTOS QUE TRANSPORTARA EL CAMION JUNTO CON SU RESPECTIVO CONTENEDOR \n ")
        
        def impresion_productos_que_se_transportan_en_camion_1(a):
            print("EL producto que se transportara en el camion es el siguiente:  {} y el tipo de contenedor en el que se transportara es {} ademas el tipo de producto es {} por lo tanto la masa es  {} obteniendo un tonelaje correspondiente de {} \n".format(a.nombre_producto, a.tipo_contenedor, a.tipo_producto, a.masa, a.peso))
            print("------------------------------------------------------------------------------------------------------------------------")
    
    producto_1_t = productos_camion(1, "plancha_cobre",2 ,24000 , 8, "Normal_Grande", "normal", "solida")
    producto_1_t.impresion_productos_que_se_transportan_en_camion_1()

    #---------------------------
    # Creacion del Histograma

    tonelaje_cada_producto = {24000} #producto1
    
    plt.hist(tonelaje_cada_producto, bins=10, color="black", rwidth=0.9)
    plt.title("tonelaje de cada producto en el camion")
    plt.xlabel("valores")
    plt.ylabel("tonelaje")
    plt.show()

def cantidad_de_vehiculos():
    barco = 1 
    tren = 1 
    avion = 1 
    camion = 1
    total = barco + tren + avion + camion
    print()
    print("CANTIDAD TOTAL DE VEHICULOS \n")
    print("la cantidad total de vehiculos es de {} ".format(barco+tren+avion+camion))
    print("------------------------------------------------")
    print("TOTAL DE CADA TIPO DE VEHICULOS \n")
    print("hay {} tipo de vehiculo acuatico ".format(barco))
    print("hay {}  tipos de vehiculos terrestres".format(tren+camion))
    print("hay {} tipo de vehiculo aereo \n".format(avion))
    
def total_vehiculos():
    barco = 1 
    tren = 1 
    avion = 1 
    camion = 1
    total = barco + tren + avion + camion
    print("hay un total de {}".format(total))
    
    
def costo_de_transporte(): #costo total del transporte, junto con su costo parcial por vehiculo
    barco = 1000000000
    tren = 10000000
    avion = 1000000 
    camion = 500000
    print("------------------------------------------------------------------------------")
    print("COSTO DEL TRANSPORTE\n")
    print("Cantidad total del costo del transporte = ${}\n".format(barco+tren+avion+camion))
    print("Total parcial del barco =  ${}\n".format(barco))
    print("Total parcial del tren = ${}\n".format(tren))
    print("Total parcial del avion = ${}\n".format(avion))
    print("Total parcial del camion = ${}\n".format(camion))
    
def interfaz_grafica():    
    class interfaz_grafica:
          
        def __init__():
            windows = tkinter.Tk()
            windows.resizable(0,0) #Impedimos redimensionar la windows
            windows.geometry("1000x568") #Tamaño por defecto
            etiqueta = Label(windows, text = total_vehiculos())
            etiqueta.grid(row=0, column=0)
            windows.title("Optimizador") #Titulo de windows
            windows = tkinter.mainloop()
    
    
      
            
def main(): # funcion principal que me ejecuta las subfunciones 
        grafico = interfaz_grafica()
        Clase_V = Vehiculos()
        Clase_C = t_contenedores()
    
#       lectura = lectura_csv()
#       Barco = distribucion_del_viaje_barco()
#       productos_del_barco = producto_barco()
#       Tren = distribucion_del_viaje_tren()
#       productos_del_tren = producto_tren()
#       Avion = distribucion_del_viaje_avion()
#       productos_del_avion = producto_avion()
#       Camion = distribucion_del_viaje_camion()
#       productos_del_camion = producto_camion() 
#       cantidad_total = cantidad_de_vehiculos()
#       costo_transporte = costo_de_transporte()
        
    

if __name__ == '__main__':
    main()
        
        
          
    
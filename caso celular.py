

'''Una empresa de venta de celulares requiere registrar los celulares que vende para mejorar la gestión de su
casa matriz, cada unidad posee un imei único, una marca, modelo y precio.
Se requiere registrar los datos de cada celular de la bodega, cuya capacidad máxima es de 500 equipos. El
imei se debe poder generar de forma aleatoria, para agilizar el registro de los datos.
Se debe poder simular una venta de un celular, cada celular se debe poder ubicar mediante su número IMEI
y se debe mostrar la marca, modelo y el precio de venta (incluye IVA), si el cliente tiene una antigüedad
mayor a 10 años se aplica un descuento del 15% sobre el total con IVA, los datos de la venta simulada se
deben mostrar de la siguiente forma:
SIMULACIÓN DE VENTA
---------------------------------------------------
IMEI: 343243432432
MARCA: SAMSUNG
MODELO: GALAXY X4
PRECIO: 190000
----------------------------------------------------
IVA: 36100
PRECIO DE VENTA: 226100
CLIENTE ANTIGUO: SI
DESCUENTO: 33915
TOTAL A PAGAR: 192185
Se debe proporcionar una opción de generación de resumen de bodega que permita mostrar la cantidad de
celulares de alta gama con precios sobre $600.000 y la valorización de celulares en bodega (suma de los
precios de cada uno).
Las funcionalidades anteriores deben estar disponibles en un menú de opciones de la siguiente forma (utilice
funciones externas): 
MENU GESTIÓN DE EMPRESA
-------------------------------------------------
1.- REGISTRAR CELULAR
2.- SIMULAR VENTA
3.- VER RESUMEN DE BODEGA
4.- SALIR
-------------------------------------------------
INGRESE SU OPCION (1-3):
Considere validar que la antigüedad este entre 0 y 30 años, que la opción de cliente antiguo sea S/N y que el precio de
cada celular esté entre 50.000 y 1.200.000'''



listaCel=[]
import random
CAPACIDAD=500
IVA=0.19
import buscar_lista

while(True):
    
        print("Menu")
        print("1.- Registrar celular")    
        print("2.- simular venta") 
        print("3.- Ver resumen de bodega") 
        print("4.- listar")
        print("4.- Eliminar")
        print("4.- Salir")
        opcion=int(input("Ingrese su opcion: "))
        if opcion not in [1,2,3,4]:
            raise ValueError
        
        if opcion == 1:
            numImei = int(input("Ingrese el IMEI")) 
            marca = input("Ingrese Marca del celular: ")
            modelo = input("ingrese modelo de equipo: ")
            precio = int(input("Ingrese el precio: ")) 
            dic = {"marca":marca, "modelo":modelo, "precio":precio, "imei":imei}

            if(len(listaCel)<CAPACIDAD):
               if()
                listaCel.append(dic)
            else:
                print("Nose puede registrar mas.........")

        if opcion == 2:
            print("simular")
            imeiBuscado = input("Ingrese el IMEI a buscar:")
            posicion = buscar_lista.buscarCelular(listaCel, imeiBuscado )
            if(posicion>=0):
                print(f"precio:{listaCel[posicion]["precio"]}")
                print(f"marca:{listaCel[posicion]["marca"]}")
                print(f"modelo:{listaCel[posicion]["modelo"]}")
                print(f"imei:{listaCel[posicion]["imei"]}")
                valorIva = listaCel[posicion]["precio"]*IVA
                antiguo = input("Es cliente antiguo? S/N:" )
                descuento = 0
                if(antiguo=="S"):
                    descuento=0.15
                else:
                    descuento=0
                valorDescuento = listaCel[posicion]["precio"]*descuento
                totalFinal = listaCel[posicion]
        elif opcion == 3:
            print("Resumen")
            cantidadAltagama = buscar_lista.altagama(listaCel)
            print(f"Cantidades de celulares alta gama {cantidadAltagama}")
            valorizacion = buscar_lista.valorizar(listaCel)
            print(f"Valorizacion de bodega{valorizacion}")
            
        elif opcion == 4:
            print("salir")
            
        elif opcion == 5:
            print("Eliminar")
            imeiBorrar = int(input("Ingrese el imei a borrar:"))
            
        elif opcion == 6:
            print("salir")

        else:
            print("error")



                        



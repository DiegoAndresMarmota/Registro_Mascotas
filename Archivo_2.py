import os
import datetime

CREAR = 1
BUSCAR = 2
ELIMINAR = 3
LISTAR = 4
ORDENAR = 5
SALIR = 0

registro_mascotas = []
#tiempo = datetime.datetime.now()
#print(tiempo.strftime('%d/%m/%Y %H:%M:%S'))

def imprimir_registro():
    #os.system('cls')
    print(f'''                    BIENVENIDOS AL REGISTRO DE MASCOTAS, 
            una empresa de soluciones digitales de Centenario S.A.
          --------------------------------------------------------
          {CREAR}) Crear nuevo registro de la mascota:
          {BUSCAR}) Buscar a la mascota registrada:
          {ELIMINAR}) Eliminar del registro completo a la mascota definida:
          {LISTAR}) Mostrar el registro completo de mascotas:
          {ORDENAR}) Ordenar el registro completo de mascotas:
          {SALIR}) Salir del registro de mascotas:
          ---------------------------------------------------------
          ''')
def crear_registro():
    print('              Crear mascota')
    nombre = input('Nombre: ')
    registro_mascotas.append(nombre)
    print(f'La mascota {nombre} ha sido agregado con éxito al registro')
  
def buscar_registro():
    print('               Buscar mascota')
    if len(registro_mascotas) >0:
        nombre = input('Nombre de la mascota buscada: ')
        if nombre in registro_mascotas:
            cantidad = registro_mascotas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = registro_mascotas.index(nombre, inicio)
                print(f' La mascota {nombre}, se encuentra en la posición {pos+1}')
                inicio = pos + 1    
        else:
            print(f'La mascota {nombre} no ha sido encontrado en el registro de mascotas.')
                  
def eliminar_registro():
    print('               Eliminar mascota')
    nombre = input('Nombre de la mascota eliminada: ')
    if len(registro_mascotas) >0:
        for i in range(len(registro_mascotas)):
            print(f'{i+1}. {registro_mascotas[i]}')
        print('0. Cancelar')
        pos = int(input(f'Posicion a eliminar (1- {len(registro_mascotas): })'))
        if 0 < pos <= len(registro_mascotas):
            registro_mascotas.pop(pos-1)
            print('Registro de mascotas eliminado con éxito')
        else:
            print('No se eliminará ninguna mascota')
    else:
        print (f'No se ha agregado la mascota {nombre} al registro de mascotas.')    

def listar_registro():
    print('               Listar mascotas:')
    if len(registro_mascotas) > 0:
        for mascotas in registro_mascotas:
            print(registro_mascotas)
    else:
        print('No se han agregado mascotas a la lista')
        
def ordenar_registro():
    print('        Ordenar mascotas:')
    if len(registro_mascotas) > 0:
        registro_mascotas.sort()
        print('El registro de mascotas ha sido ordenado satisfactoriamente.')
    else:
        print('No se han agregado mascotas a la lista.')
        
def main():
    continuar = True
    while continuar:
        imprimir_registro()
        opc = int(input('Selecciona una opción: '))
        os.system('cls')
        if opc == CREAR:
            crear_registro()
        elif opc == BUSCAR:
            buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == LISTAR:
            listar_registro()
        elif opc == ORDENAR:
            ordenar_registro()
        elif opc == SALIR:
            print('Nos vemos. Buen día ')
            continuar = False
        else:
            print('Opción no válida. Buen día. ')
        input('Presiona la tecla ENTER para continuar.')

if __name__ == '__main__':
    main()
                
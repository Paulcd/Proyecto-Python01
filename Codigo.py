
#Trabajo final, perfecto.
import timeit


cola=[
     [2,'Recordatorio de simulacro'],
     [1,'Junta general presentarse antes de las 8:00'],
     [3,'Cuidado con piso mojado'],
     [4,'Oye Pepe que tal la reuna???'],
     [2,'Adjuntar ficheros antes de retirarse'],
     [4,'No, tío, con fé clasificamos'],
     [1,'Error crítico en modulo EVA01'],
     ]


def selsort(lista):
  for x in range(len(lista) - 1):     #N

    minimo = x                        #C
    
    for y in range(x+1 , len(lista)): #N
      if lista[y] < lista[minimo]:    #C
        minimo = y#C

    auxiliar = lista[x]#C
    lista[x] = lista[minimo]#C
    lista[minimo] = auxiliar#C

  return lista#C


def impmensajes(cola):
  print('[prioridad][mensaje]')
  for i in range(len(cola)): #N (linear)
    print(f'{cola[i][0]}:         {cola[i][1]}')
          
 
def menu():
    global cola
    aceptado=[1,2,3,4,0]
    print(" ") 
    print("Opciones:")
    print(f'1: Insertar\n2: Eliminar\n3: Ordenar\n4: Ver mensajes\n0: Salir')
    inp = int(input ('Ingrese opción: '))
  
    if inp not in aceptado:
        print(" ")
        print(" ")
        print("Ingrese la opcion correcta Por favor:")
        menu()
       
        
    elif inp ==1:
        inpt=int(input('Ingrese prioridad: '))
        inpt2=input('Ingrese un mensaje: ')
        cola.insert(0,[inpt,inpt2])
        print ('Se insertó mensaje!')
        input()
        menu()
        
    elif inp ==2:
        cola.pop()
        print ('Se eliminó el ultimo mensaje!')
        input()
        menu()
        
    elif inp ==3:
        print('Se ordenó la cola!')
        selsort(cola)
        input()
        menu()
        
    elif inp ==4:
        impmensajes(cola)
        input()
        menu()
        
    elif inp == 0 :  
      print("Saliendo...")
      
      exit(0)
     

def test():
  selsort([])

if __name__ == '__main__':
    print('\n'+"Timeit:",timeit.timeit("test()", setup= "from __main__ import test", number=10))        


menu()      






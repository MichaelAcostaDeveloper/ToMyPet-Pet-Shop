#Definicion del metodo run()
"""Este metodo da la bienvenida a todos los usuarios"""
def run():
          while True:
                    print(10*'#'+" Bienvenidos a ToMyPet "+10*'#')
                    opcion_ingreso = int(input('''Selecciona el tipo de usuario:
                    1. Manager.
                    2. Cliente.
                    3. Salir.
                    ->'''))
                    if opcion_ingreso == 1:
                              user = input('Ingrese su usuario: ')
                              passw = input('Ingrese su password: ')
                              print('Bienvenido '+user+'.')
                              #CODIGO PARA INGRESAR AL SITIO COMO MANAGER
                              break #hace que el ciclo termine en este punto
                    elif opcion_ingreso == 2:
                              print('''Estimado cliente seleccione la opcion que necesita:
                              1. Creacion de codigo QR.
                              2. Reactivacion del codigo QR.
                              3. Localizadores y app.
                              4. Alimentacion perruna.
                              ->''')
                              #CODIGO DE EVALUACION DE LAS OPCIONES
                              break #hace que el ciclo  termine en este punto
                    elif opcion_ingreso == 3:
                              print('Un placer servirle!')
                              return False #cierra el ciclo while
                    else:
                              print('Ingrese una opcion valida!!!')





#Creacion del punto de partida del proyecto para registro de mascotas perrunas
if __name__=='__main__':
          run()
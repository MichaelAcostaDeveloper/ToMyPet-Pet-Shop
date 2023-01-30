"""
En este proyecto tenemos tres ramas en local main, master y dev.
Cualquier cambio o actualizacion a nivel de codigo se lo debe hacer en la rama dev.
Los cambios se deben mergear a la rama master.
Posteriormente se deden mergear a la rama main.
Cuando los cambios esten en la rama local main, usar git push para pasarlo a remoto en github."""
#Definicion del metodo creationPassword()
'''Este metodo permite crear password con 5 caracteres'''
def creationPassword():#este metodo retorna el password validado
          while True:
                    password_cero = input ('Ingresa tu password (debe tener 5 caracteres): ')
                    if len(password_cero) == 5:
                              break
                    else:
                              print('Ingresa un password correcto!!!')
          return password_cero

#Definicion del metodo userCreation()
'''Este metodo permite crear un usuario'''
def userCreation(): #al final este metodo permite crear un usuario como diccionario y colocarlo en una lista de usuarios
          print(5*'*'+'Bienvenido a toMtPet'+5*'*'+'\n')
          print('En este modulo crearemos tu cuenta personal')
          name_cero = input('Ingresa tu nombre: ')
          lastname_cero = input('Ingresa tu apellido: ')
          email = input ('Ingresa tu correo electronico: ')
          password_new = creationPassword()
          user_toMyPet = {'name':name_cero,
                              'last name': lastname_cero,
                              'email' : email,
                              'password' : password_new}
          list_users.append(user_toMyPet)
          print('Felicidades... hemos creado su cuenta personal!\n\n')

#Definicion del metodo run()
"""Este metodo es el menu principal de la app"""
def run():
          while True:
                    print(10*'#'+" Bienvenidos a ToMyPet "+10*'#')
                    opcion_ingreso = int(input('''Selecciona la opcion de tu preferencia:
                    1. Manager.
                    2. Cliente.
                    3. Crear usuario
                    4. Salir.
                    ->'''))
                    if opcion_ingreso == 1:
                              user = input('Ingrese su usuario: ')
                              passw = input('Ingrese su password: ')
                              print('Bienvenido '+user+'.')
                              #CODIGO PARA VALIDAR USUARIO
                              #cODIGO PARA PRESENTAR LO QUE QUIERE HACER EL MANAGER
                              break #hace que el ciclo termine en este punto
                    elif opcion_ingreso == 2:
                              print('''Estimado cliente seleccione la opcion que necesita:
                              1. Creacion de codigo QR.
                              2. Reactivacion del codigo QR.
                              3. Localizadores y app.
                              4. Alimentacion perruna.
                              ->''')
                              #CODIGO PARA VALIDAR USUARIO
                              #cODIGO PARA PRESENTAR LO QUE QUIERE HACER EL CLIENTE
                              break #hace que el ciclo  termine en este punto
                    elif opcion_ingreso == 3:
                              userCreation()
                              print(list_users)
                    elif opcion_ingreso == 4:
                              print('Un placer servirle!')
                              return False #cierra el ciclo while
                    else:
                              print('Ingrese una opcion valida!!!')





#Creacion del punto de partida del proyecto para registro de mascotas perrunas
if __name__=='__main__':
          list_users = []
          run()
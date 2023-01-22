#Definicion del metodo run()
"""Este metodo da la bienvenida a todos los usuarios"""
def run():
          print(10*'#'+" Bienvenidos a ToMyPet "+10*'#')
          opcion_ingreso = int(input('''Selecciona el tipo de usuario:
          1. Manager.
          2. Cliente.
          ->'''))
          if opcion_ingreso == 1:
                    user = input('Ingrese su usuario: ')
                    passw = input('Ingrese su password: ')
                    print('Bienvenido '+user+'.')
          else:
                    print('''Estimado cliente seleccione los que necesita:
                    1. Creacion de codigo QR.
                    2. Reactivacion del codigo QR.
                    3. Localizadores y app.
                    4. Alimentacion perruna.
                    ->''')




#Creacion del punto de partida del proyecto para registro de mascotas perrunas
if __name__=='__main__':
          run()
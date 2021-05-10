import csv
import re

class Email: 
   __idCuenta: " "
   __dominio:" "
   __tipoDominio: " "
   __passw:" "

   def __init__(self, idCuenta="", dominio="", tipoDominio="", passw=""):
      
      self.__idCuenta=idCuenta
      self.__dominio=dominio
      self.__tipoDominio=tipoDominio
      self.__passw=passw
   def cargarDatos(self):
      self.__idCuenta= input("idCuenta:")
      self.__dominio=input("dominio:")
      self.__tipoDominio=input("tipoDominio:")
      self.__passw=input("passw:")  
   def retornaEmail(self):
        return f'{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}'
   def mostrarDatos(self):
      print(' ID Cuenta {}, Dominio {}, Tipo {}, Contraseña {} '.format(self.__idCuenta, self.__dominio, self.__tipoDominio, self.__passw))
   def getDominio(self):
       return ""+self.__dominio
   
   def verificarCorreo(self, correo):
        band=None
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            band=True
        else:
            band=False
        return band
   def crearCuenta (self, correo):
            aux = correo.split('@')
            aux_1 = aux[1].split('.')
            password = input('Ingresar contraseña : ')
            unEmail = Email(aux[0],aux_1[0],aux_1[1],password)
            return unEmail

   def cambiarPass(self):
       print("Cambio de contraseña")
       contrasenaActual=input("Ingresar Contraseña Actual:")
       if (self.__passw==contrasenaActual):
          print("Las contraseñas coincien")
          self.__passw=input("ingrese la nueva contraseña:")
       else: print("La contraseña ingresada no es correcta")
   def verificarCorreo(self,correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):

            return True
        else:
            return False

def contadorDominio():
    dominio=input("Ingresar Dominio a buscar:")
    contador = 0
    archivo = open('Emails.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        if dominio == fila[1]:
           contador=contador+1
    print ("La cantidad de dominios es:")
    print (contador)
    return contador
    archivo.close()
def test():
    testInstancia = Email('','','','')
    testcorreo = "matias@gmail.com"#valido
    valido = testInstancia.verificarCorreo(testcorreo)
    if valido:
        print("El Correo es Correcto")
    else:
        print("El Correo no es Correcto")
  


if __name__ == '__main__':
    test()
    nombre=input("Ingresar Nombre:")
    correoElectronico = input('Ingrese un correo electrónico: ')
    mailOtro=Email()
    if mailOtro.verificarCorreo(correoElectronico)==True:
          mailOtro= mailOtro.crearCuenta(correoElectronico)
          print('Estimado {} te eviaremos tu mensaje a la direccio {}' .format(nombre,mailOtro.retornaEmail()))
          mailOtro.mostrarDatos()
          mailOtro.cambiarPass()
          contadorDominio()
    else:
      print('El mail que ingresó es inválido')

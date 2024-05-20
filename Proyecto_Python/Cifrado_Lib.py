# realizado con la biblioteca cryptography (pip install cryptography)

from cryptography.fernet import Fernet

def generar_clave():
    clave = Fernet.generate_key() 
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)


def cargar_clave():
    return open("clave.key","rb").read()


generar_clave()

clave = cargar_clave()

mensaje = input("Inserte su mensaje a encriptar: ").encode()
f = Fernet(clave)

encriptado = f.encrypt(mensaje)

print("El mensaje encriptado es: ",encriptado)

#proceso de desencriptado

desencriptado = f.decrypt(encriptado)

print("El mensaje desencriptado es: ",desencriptado)

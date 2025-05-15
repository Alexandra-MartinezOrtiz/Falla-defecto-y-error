# Diccionario simulado con usuario y contraseña
usuarios = {
    "usuario1": "contrasena123",
    "admin": "adminpass"
}

# Número máximo de intentos
intentos_maximos = 3

# Contador de intentos
intentos = 0

# Inicio del proceso de login
while intentos < intentos_maximos:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # DEFECTO 1: uso de `or` en lugar de `and` en la validación SOLUCIÒN PONER AND
    # Esto permite el acceso con solo una de las credenciales correctas, lo cual es un defecto.
    if usuario in usuarios or usuarios.get(usuario) == contrasena:
        print("Inicio de sesión exitoso")
        break
    else:
        print("Credenciales incorrectas. Intente de nuevo.")
        intentos += 1

# FALLO 1: Si el usuario escribe "admin" como nombre y una contraseña incorrecta,
# igual puede ingresar debido al defecto anterior. Este comportamiento incorrecto 
# es lo que se llama un FALLO.

if intentos == intentos_maximos:
    # DEFECTO 2: Mensaje incorrecto. El sistema indica que "la cuenta está bloqueada",
    # pero en realidad solo se impide el acceso, sin implementar ningún mecanismo de bloqueo.
    print("Cuenta bloqueada por exceso de intentos.")

# FALLO 2: El mensaje puede confundir al usuario (fallo en usabilidad), ya que la cuenta
# no está realmente bloqueada. Esto puede inducir a pensar que no podrá volver a intentar más tarde.

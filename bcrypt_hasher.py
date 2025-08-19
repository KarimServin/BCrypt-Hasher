import bcrypt

# Solicita el string al usuario
password = input("Ingrese el string a hashear: ")

# Genera el hash con bcrypt
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Muestra el hash generado
print("Hash bcrypt:", hashed.decode())

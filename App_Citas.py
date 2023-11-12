import random
from datetime import datetime

#Clase persona
class Persona:
    def __init__(self, nombres, apellidos, fecha_nacimiento, sexo, cedula):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.cedula = cedula

#Calcular edad
def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    nacimiento = datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

#Método CRUD (Agregar - Actualizar - Eliminar)
def agregar_usuario(usuarios):
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-YYYY): ")
    sexo = input("Sexo (M/F): ").upper()
    cedula = input("Cédula: ")

    # Validar edad
    if calcular_edad(fecha_nacimiento) < 18:
        print("Debes ser mayor de 18 años para registrarte.")
        return

    # Validar sexo
    if sexo not in ('M', 'F'):
        print("Sexo no válido.")
        return

    # Validar cédula única
    if any(usuario.cedula == cedula for usuario in usuarios):
        print("Ya existe un usuario con esa cédula.")
        return

    nuevo_usuario = Persona(nombres, apellidos, fecha_nacimiento, sexo, cedula)
    usuarios.append(nuevo_usuario)
    print("Usuario agregado correctamente.")

def actualizar_usuario(usuarios):
    cedula = input("Ingresa la cédula del usuario que deseas actualizar: ")
    usuario_existente = next((usuario for usuario in usuarios if usuario.cedula == cedula), None)

    if usuario_existente:
        print(f"Datos actuales del usuario ({cedula}):")
        print(f"Nombres: {usuario_existente.nombres}")
        print(f"Apellidos: {usuario_existente.apellidos}")
        print(f"Fecha de nacimiento: {usuario_existente.fecha_nacimiento}")
        print(f"Sexo: {usuario_existente.sexo}")

        nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener): ")
        nuevo_apellido = input("Nuevo apellido (dejar en blanco para mantener): ")
        nueva_fecha_nacimiento = input("Nueva fecha de nacimiento (DD-MM-YYYY, dejar en blanco para mantener): ")
        nuevo_sexo = input("Nuevo sexo (M/F, dejar en blanco para mantener): ").upper()

        if nuevo_nombre:
            usuario_existente.nombres = nuevo_nombre
        if nuevo_apellido:
            usuario_existente.apellidos = nuevo_apellido
        if nueva_fecha_nacimiento:
            usuario_existente.fecha_nacimiento = nueva_fecha_nacimiento
        if nuevo_sexo:
            usuario_existente.sexo = nuevo_sexo

        print("Usuario actualizado correctamente.")
    else:
        print("No se encontró ningún usuario con esa cédula.")

def eliminar_usuario(usuarios):
    cedula = input("Ingresa la cédula del usuario que deseas eliminar: ")
    usuario_existente = next((usuario for usuario in usuarios if usuario.cedula == cedula), None)

    if usuario_existente:
        usuarios.remove(usuario_existente)
        print("Usuario eliminado correctamente.")
    else:
        print("No se encontró ningún usuario con esa cédula.")


#Formar parejas
def formar_parejas(usuarios):
    hombres = [usuario for usuario in usuarios if usuario.sexo == 'M']
    mujeres = [usuario for usuario in usuarios if usuario.sexo == 'F']

    if len(hombres) > len(mujeres):
        print("Se necesitan más mujeres para formar parejas.")
        restantes_hombres = hombres[len(mujeres):]
        random.shuffle(mujeres)

        parejas = list(zip(hombres[:len(mujeres)], mujeres))

        print("Parejas formadas:")
        for pareja in parejas:
            print(f"Pareja: {pareja[0].nombres} {pareja[0].apellidos} y {pareja[1].nombres} {pareja[1].apellidos}")

        print("Hombres sin pareja:")
        for hombre in restantes_hombres:
            print(f"{hombre.nombres} {hombre.apellidos}")

    elif len(mujeres) > len(hombres):
        print("Se necesitan más hombres para formar parejas.")
        restantes_mujeres = mujeres[len(hombres):]
        random.shuffle(hombres)

        parejas = list(zip(hombres, mujeres[:len(hombres)]))

        print("Parejas formadas:")
        for pareja in parejas:
            print(f"Pareja: {pareja[0].nombres} {pareja[0].apellidos} y {pareja[1].nombres} {pareja[1].apellidos}")

        print("Mujeres sin pareja:")
        for mujer in restantes_mujeres:
            print(f"{mujer.nombres} {mujer.apellidos}")

    else:
        random.shuffle(hombres)
        random.shuffle(mujeres)

        parejas_guardadas = list(zip(hombres, mujeres))

        if len(parejas_guardadas) > 0:
            print("Parejas unidas:")
            for pareja in parejas_guardadas:
                print(f"Pareja: {pareja[0].nombres} {pareja[0].apellidos} y {pareja[1].nombres} {pareja[1].apellidos}")
        else:
            print("No hay suficientes parejas guardadas.")


usuarios = []

#Menú
while True:
    print("\nMenú:")
    print("1. Agregar usuario")
    print("2. Actualizar usuario")
    print("3. Eliminar usuario")
    print("4. Formar parejas")
    print("0. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        agregar_usuario(usuarios)
    elif opcion == '2':
        actualizar_usuario(usuarios)
    elif opcion == '3':
        eliminar_usuario(usuarios)
    elif opcion == '4':
        formar_parejas(usuarios)

    elif opcion == '0':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

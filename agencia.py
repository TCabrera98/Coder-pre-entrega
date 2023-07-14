from django.db import models 

print("\n--- AUTOMOTORES CABRERA ---")

print("¡Bienvenido a nuestra agencia de autos! Estamos comprometidos en ayudarte a encontrar el auto perfecto para ti. Nos complace ofrecerte la posibilidad de solicitar un presupuesto sin cargo. Queremos facilitar al máximo tu experiencia de compra de automóviles. Una vez que nos proporciones esta información, nuestro equipo de expertos estará encantado de generar un presupuesto adaptado a tus necesidades y preferencias.")

# Definiendo CLASE 1

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.ciudad = input("Ingrese la ciudad en la cual vive: ")
        self.email = input("Ingrese su correo electrónico + número telefónico seguido del correo: ")
        self.edad = input("Ingrese su edad: ")

        if int(self.edad) >= 18:
            print("Puedes continuar con la gestión hacia tu nuevo auto!")
        else:
            print("Nuestra política de privacidad no permite que los menores de edad realicen actos jurídicos sin autorización de sus responsables.") 
 



persona = Persona()

# Definiendo CLASE 2
class Auto:
    def __init__(self):
        self.marca = input("Ingrese la marca de su auto: ")
        self.modelo = input("Ingrese el modelo de su auto: ")
        self.km = input("Ingrese los KM que tiene su auto: ")

auto = Auto()


# Definiendo CLASE 3
class ComprarAuto:
    def __init__(self):
        self.marca = input("Ingrese la marca del auto que desea comprar: ")
        self.modelo = input("Ingrese el modelo (usado o 0km): ")
        self.color = input("Ingrese el color que desea comprar: ")

comprar_auto = ComprarAuto()

print("\n--- Datos personales ---")
print(f"Nombre: {persona.nombre}")
print(f"Apellido: {persona.apellido}")
print(f"Fecha de nacimiento: {persona.fecha}")
print(f"Ciudad: {persona.ciudad}")
print(f"Email y número telefónico: {persona.email}")


print("\n--- Datos de su auto ---") 
print(f"Marca: {auto.marca}")
print(f"Modelo: {auto.modelo}")
print(f"Kilómetros: {auto.km}")

print("\n--- Datos del auto de interés ---")
print(f"Marca: {comprar_auto.marca}")
print(f"Modelo: {comprar_auto.modelo}")
print(f"Color: {comprar_auto.color}")

opcion1 = input("¿Desea confirmar la operación? (Si/No): ")

if opcion1 == "Si":
    print("Ha quedado exitosamente registrado en nuestra base de datos. En un plazo de 48 horas hábiles, uno de nuestros representantes se comunicará con usted para continuar con el proceso. Recuerde que la operación no tiene ningún tipo de cargo.")
elif opcion1 == "No":
    print("Saliste del sistema")

opcion2 = input("¿Desea recibir más información sobre nuestros servicios? (Si/No): ")

if opcion2 == "Si":
    print("Nuestro equipo estará encantado de brindarle toda la información que necesite. No dude en contactarnos.")
elif opcion2 == "No":
    print("Gracias por visitarnos. ¡Esperamos poder ayudarte en el futuro!")


print("\n--- AUTOMOTORES CABRERA ---") 
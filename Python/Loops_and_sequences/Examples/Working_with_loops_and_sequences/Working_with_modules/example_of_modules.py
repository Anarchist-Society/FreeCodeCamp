from math import radians, sin, cos
import datetime

print('What Is the Python Standard Library, and How Do You Import a Module?\n')

print('Ejemplo de usar funciones de la libreria math:')
angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

print('\nEjemplo de usar la clase datetime:')
birthday = datetime.date(1969, 12, 15)
print(birthday)
print(birthday.day)
print(birthday.month)
print(birthday.year)

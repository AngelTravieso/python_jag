name = 'Angel Travieso'
course = 'Curso de python'

# convertir a mayuscula
name_upper = name.upper()

print(name == name_upper)

print(name_upper)
print(name)

# convertir a minuscula
print(course.lower())

words = 'curso de python'

# Primera letra en mayuscula
print(words.capitalize())

# Capitalizar cada letra
print(words.title())

words = '     hola angel     '
# Parecido al trim()
print(words.strip())

# left trim
print(words.lstrip())

# right trim
print(words.rstrip())

# replace reemplaza parte del texto
text = 'Hola Java'
print(text)
new_text = text.replace('Java', 'Python')
print(new_text)

text = 'Angel,Travieso,Java,DotNet'
data_list = text.split(',')
print(data_list)
print(data_list[0])
print(data_list[1])
print(data_list[2])

data = ['Angel', 'Travieso', ' Java', 'DotNet']
text = '/'.join(data)
print(text)

# Buscar en una cadena
text = 'Hola, Angel que tal como estas!'
print(text.find("Angel"))

# Devuelve el indice mas bajo donde coincida la busqueda
# Arroja excepcion si no encuentra (esta es una diferencia con find)(
print(text.index('como'))

# Verificar si el string empieza o termina con un string especifico
print(text.startswith('Hola'))
print(text.endswith('estas!'))

number = '1234'
decimal = '1234.10'
text = 'Python'
mix = 'Python3'

print(number.isnumeric())
print(number.isdigit())
print(decimal.isdecimal())
print(text.isalnum())
print(mix.isalpha())
print(text.isalpha())

text = '   hola Angel como estas, bienvenido al curso de Python!   '
text_clean = text.strip().capitalize().title()
print(text_clean)

new_text = text_clean.replace('Curso De Python', 'Curso de Python3')
print(new_text)

words = new_text.split()
print(words)
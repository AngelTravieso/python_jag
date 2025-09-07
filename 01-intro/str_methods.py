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


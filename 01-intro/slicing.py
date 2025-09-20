text = 'Angel Travieso'

# Desde:Hasta:De cuanto a cuanto
print(text[0:6:1])

# Del caracter 6 en adelante
print(text[6:])

# Del comienzo hasta el 6
print(text[:6])

# Toma todo
print(text[::])

# Desde al principio al final pero a la inversa, al reves
print(text[::-1])

text = 'Python'
print(text[0:4])
print(text[:4])
print(text[2:])
print(text[::3])

text = "Hola Mundo"
new_text = text[:5] + text[5:].replace('Mundo', 'Python')
print(new_text)

text = 'Python es genial'
parts = text.split()
parts2 = parts[:2]
print(parts)
print(parts2)
parts_reverse = parts[::-1]
print(parts_reverse)
text_reverse = ' '.join(parts_reverse)
print(text_reverse)

text = 'Python'
print(text[:2].lower() + text[2:].upper())

text = '   Hola Python  '
print(text.strip()[:5])
print(text.strip()[5:])


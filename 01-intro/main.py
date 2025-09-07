
def sayHello(name):
    return print(f'Hello {name}')

# Esto es para evitar que se llame el codigo dentro de main cuando se importa en un modulo
if __name__ == '__main__':
    print(f'Hi, World')
    sayHello("Angel")
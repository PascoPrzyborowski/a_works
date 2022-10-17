

def f(x, y):
    return x + y


print(f(3,4))

g = f

print(g(3,4))

def greet(f, name):
    print(f'Hello{f(name)}')

def low_name(name):
    return name.lower()

greet(lambda n : n.upper(), 'pasco')
greet(lambda n : n.lower(), 'pasco')
greet(low_name, 'PASCO')


def greet2(type):
    if type == 'informal':
        def informal_greet(name):
            return f'Hi {name}'
        return informal_greet

    elif type == 'formal':
        def formal_greet(name):
            return f'Hello {name}'
        
        return formal_greet

    else:
        def simple_greet(name):
            return f'Hi'
        
        return simple_greet


f = greet2('informal')
print(f('Pasco'))
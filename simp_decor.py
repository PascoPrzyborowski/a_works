


def annoy_deco(f):
    def decor_func(*args, **kwargs):
        print('I will not do!')
    return decor_func


#@annoy_deco
def greet(name):
    print(f'Hi {name}')

greet('Pasco')

#@annoy_deco
def sum_1(x,y):
    return x + y

sum_1(3,4)


def annoy_deco2(f):
    def decor_func(*args, **kwargs):
        print('I will do!')
        f(*args, **kwargs)
        print('Done!')
    return decor_func


@annoy_deco2
def greet3(name):
    print(f'Hi {name}')

greet3('Pasco')

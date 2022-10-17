




authorized = True

def is_authorized(f):
    def deco_func(*args, **kwargs):
        if authorized:
            f(*args, **kwargs)
        else:
            print('not decleared!')
    return deco_func

@is_authorized
def list_user():
    print('Pasco\nJohn\nKathy')

@is_authorized
def app_version():
    print('ver 1,0')

def details(f):
    def func(*args, **kwargs):
        details = '---'
        details = f(*args, **kwargs)
        details = 'version 1,0'
        details = '---'
        return details
    return func

def user_data():
    return 'name: not'

list_user()
app_version()
#print(user_data())
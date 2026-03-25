# positional-only argument
def wish(name, message, /):
    print(message, name)


wish('Steve', 'Hi')
#wish(name='Steve', message='Hi')

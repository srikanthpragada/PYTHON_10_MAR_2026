# positional-only argument
def wish(name : str, message : str, /) -> None:
    print(message, name)


wish('Steve', 'Hi')
#wish(name='Steve', message='Hi')

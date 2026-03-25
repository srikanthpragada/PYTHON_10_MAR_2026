# keyword-only argument
def wish(*, message, name):
    print(message, name)


# wish('Steve', 'Hi')
wish(name='Steve', message='Hi')

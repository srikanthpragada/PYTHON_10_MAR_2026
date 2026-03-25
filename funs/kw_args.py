def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


show(a = 10, b = 20)
show(name = 'Python', ver = 3.12)

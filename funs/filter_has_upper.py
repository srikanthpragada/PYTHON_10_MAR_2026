names = ['Java', 'Python', 'C', 'SQL', 'javascript', 'Php']


def has_upper(name):
    for c in name:
        if c.isupper():
            return True
    return False


for name in filter(has_upper, names):
    print(name)

TITLE = "Srikanth Technologies"

def has_upper(st : str) -> bool:
    for c in st:
        if c.isupper():
            return True
    return False

def has_digit(st : str) -> bool:
    for c in st:
        if c.isdigit():
            return True
    return False


# Run this code only when module is run as script and not imported
if __name__ == '__main__':
    # Run only when it is run as script
    print(has_upper('java'))

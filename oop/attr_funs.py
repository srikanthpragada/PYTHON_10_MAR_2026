class Player:
    def __init__(self, name):
        self.name = name


p = Player("Dhoni")
print(getattr(p, 'name'))
# print(p.game)
print(getattr(p, 'game', 'Cricket'))
print(hasattr(p, 'game'))
setattr(p, 'age', 40)
print(p.__dict__)
delattr(p, 'age')
print(p.__dict__)

print(Player.__module__)
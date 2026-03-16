# Take a number and display its table

num = int(input("Enter a number :"))

for i in range(1, 21):
    print(f"{num:3} * {i:2} = {num * i:5}")


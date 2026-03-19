# Take 10 numbers and print even numbers in sorted order first and then odd numbers

evens = []
odds = []

for i in range(10):
    n = int(input("Enter a number :"))
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

evens.sort()
odds.sort()

for n in evens + odds:
    print(n)

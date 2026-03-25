def wishall(*names, message = 'Hi'):
   for n in names:
       print(message, n)


wishall('Jack', 'Andy', message = 'Hello' )
wishall('Jack', 'Andy', 'Bill')
wishall()

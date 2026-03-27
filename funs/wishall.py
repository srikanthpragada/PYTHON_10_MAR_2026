def wishall(*names, message = 'Hi'):
   """
   Wishes all users
   :param names: List of users
   :param message: Message to use for wishing
   :return: None
   """
   for n in names:
       print(message, n)


wishall('Jack', 'Andy', message = 'Hello' )
wishall('Jack', 'Andy', 'Bill')
wishall()

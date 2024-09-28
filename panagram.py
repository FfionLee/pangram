user=input('Enter a sentence:')
alphabet=set('abcdefghijklmnopqrstuvwxyz')

if alphabet.issubset(user):
    print('It is a panagram')
else:
    print('It is not a panagram')
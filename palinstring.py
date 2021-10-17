mystr=input('Enter the string:')
revstr=mystr[::-1]
print(revstr)
if mystr==revstr:
    print('Palindrome')
else:
    print('Not Palindrome')
def sum_of_squares(n):
    Sum = 0
    for i in range(n+1):
        Sum += i**2
    return Sum

print sum_of_squares(4)

def is_excited(text):
    upper = 0
    exclam = 0
    unletters = 0
    for i in text:
        if i.isupper():
            upper +=1
        elif i=='!':
            exclam +=1
        elif not i.isalpha():
            unletters += 1
        else:
            pass
    if exclam >=1:
        return True
    elif upper > (len(text)-unletters)/2.0:
        return True
    else:
        return False

print is_excited('BIG LETTERS')
print is_excited('exclam!')
print is_excited('BiG ')
print is_excited('not QUITE half')
print is_excited('HALF EXCEPT for spaces')

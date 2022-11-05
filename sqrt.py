def f1():
    a = (str(179)*50)
    print(int(a)**2)

def f2():
    n = int(input('Колво учеников: '))
    k = int(input('Колво яблок: '))

    if n < 10000 and k < 10000 and n > 0 and k > 0:
        print(k // n)

    else:
        print('Колво не дожно превышать 10000, и не меньше 0!')

def f3():
    a = int(input('1: '))
    b = int(input('2: '))
    c = int(input('3: '))

    if a == b and b == c:
        print(3)
    elif a == b or b == c or c == a:
        print(2)
    else:
        print(0)

def f4():
    a = 'oofoofoofoofoo'
    try: print(a.index('f'), len(a) - (a[::-1].index('f')+1))
    except ValueError: print()


def f5():
    a = 'In the hole in the ground there lived a hobbit'
    b = a.index('h')
    c = a.rfind('h')
    print(a[:b]+a[c+1:])


def f6():
    a = [_ for _ in input('Enter: ')]
    while len(a) != 0:

        if a[0] == '(' and a[-1] == ')' or a[0] == '[' and a[-1] == ']' or a[0] == '{' and a[-1] == '}':
            del a[0]
            del a[-1]
            print('List:', a)
        elif a[0] == '(' and a[-1] != ')' or a[0] == '[' and a[-1] != ']' or a[0] == '{' and a[-1] != '}':
            print('No')
            break
        else:
            print('No!')
            break







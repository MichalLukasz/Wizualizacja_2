import sys as system

print('Zadanie 1')
print('Napisz jakieś zdanie.')
x = input()
print(x)
print('Ilość powtórzeń litery a: ' + str(x.count('a')))

print('Zadanie 2')
system.stdout.write("Podaj 3 liczby: \n")
a = system.stdin.readline()
b = system.stdin.readline()
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
system.stdout.write('Wynik (a^b)+c: ' + str((a ** b) + c))

print('\nZadanie 3')
system.stdout.write("Podaj 3 liczby: ")
x = system.stdin.readline()
y = system.stdin.readline()
z = system.stdin.readline()
x = int(x)
y = int(y)
z = int(z)

liczba = 0
if x >= y:
    if x >= z:
        liczba = x
        print('\nNajwiększa liczba: ' + str(liczba))
if y >= x:
    if y >= z:
        if liczba != x:
            liczba = y
            print('\nNajwiększa liczba: ' + str(liczba))
if z >= x:
    if z >= y:
        if liczba != x & liczba != y:
            liczba = z
            print('\nNajwiększa liczba: ' + str(liczba))

print('\nZadanie 4')
lista = [5, 2, 6.7, 10, 5.55, 2.3, 4]
for x in lista:
    print(pow(x, 2))

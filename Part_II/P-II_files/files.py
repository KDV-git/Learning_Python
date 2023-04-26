myfile = open('myfile.txt', 'w')

poop = myfile.write('hello text file\n')
print(poop)
poop = myfile.write('goodbye text file\n')
print(poop)

myfile.close()

myfile = open('myfile.txt')

print(repr(myfile.readline()))
print(repr(myfile.readline()))
print(repr(myfile.readline()))
print(repr(myfile.readline()))

print('\n')

myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(repr(myfile.read()))

myfile.seek(0)
print(len(myfile.read()))

print('\n')

# кратко о двоичных файлах
data = open('mybinfile.bin', 'wb')
data.write(b'\x00\x00\x00\x07spam\x00\x08')
data.close()

data = open('mybinfile.bin', 'rb')
print(repr(data.read()))

data.seek(0)
print(data.read())

data.seek(0)
print(data.read()[4:8])

print('\n')

# Хранение объектов в файлах: преобразования
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('mydatafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('mydatafile.txt').read()
print(repr(chars))
print(chars)

F = open('mydatafile.txt')
line = F.readline()
print(repr(line))
print(line)
print(repr(line.rstrip()))
print(line.rstrip())

print('\n')

line2 = F.readline()
print(repr(line2))
parts = line2.rstrip().split(',')
print(parts)
print(type(parts[0]))

int_parts = [int(x) for x in line2.split(',')]
print(int_parts)
print(type(int_parts[0]))

print('\n')

line3 = F.readline()
print(repr(line3))

objects = [eval(x) for x in line3.split('$')]
print(objects)
print(type(objects[0]))
print(type(objects[1]))

print('\n')

# Модуль picle (расширяется модулем shelve)
import pickle

D = {'a': 1, 'b': 2}
F = open('mypklfile.pkl', 'wb')
pickle.dump(D, F)
F.close()

F = open('mypklfile.pkl', 'rb')
print(repr(F.read()))

F.seek(0)
E = pickle.load(F)
print(E)

print('\n')

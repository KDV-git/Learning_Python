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

# Кратко о двоичных файлах
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

# Хранение объектов Python в формате JSON
import json

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)

S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)

print(O == rec)

print('\n')

json.dump(rec, fp=open('myjsonfile.txt', 'w'), indent=4)
print(open('myjsonfile.txt').read())

P = json.load(open('myjsonfile.txt'))
print(P)

print('\n')

# Хранение упакованных двоичных данных: модуль struct
import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('mybinfile.bin', 'wb')
file.write(packed)
file.close()

data = open('mybinfile.bin', 'rb').read()
print(data)

l = list(data)
print(l)

unp_data = struct.unpack('>i4sh', data)
print(unp_data)

print('\n')

# Диспетчеры контекстов для файлов (Гарантия закрытия файла, сброса буфера и освобождения памяти)
with open('myfile.txt') as myfile:
    for line in myfile:
        print(repr(line))
        print(line)

myfile = open('myfile.txt')
try:
    for line in myfile:
        print(repr(line))
        print(line)
finally:
    myfile.close()

print('\n')
path = 'C:\test\new'
print(path)

giga_path = r'C:\test\new'
print(giga_path)

alp_path = 'C:\\test\\new'
print(alp_path)

uni_str = 'sp\xc4m'
print(uni_str)

code_str = 'sp\xc4\u00c4\U000000c4m'
print(code_str)

byte_str = b'a\x01c'
print(type(byte_str))
print(byte_str)

print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))

print('\n---\n')

x = ord('s')
print(x)
print(chr(x))
print('\n')

s = "3"
for num in range(10):
    s = chr(ord(s) + 1)
    print(s)

print('\n')

# Преобразование двоичных чисел в целое число с помощью ord
B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)
print(int('1101', 2))

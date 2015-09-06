__author__ = 'huangw-d'

obj1 = {'a': 1, 'b': 2}
F = open("myfile.txt", 'wb')
import pickle

pickle.dump(obj1, F)
F.close()

R = open('myfile.txt', 'rb')
E = pickle.load(R)
print(R)

# file1 = open('data.bin', 'wb')
# import struct
# data1 = struct.pack('>i4sh', 7, 'spam', 8)
# print(data1)
# file1.Write(data1)
# file1.close()
# file2 = open('data.bin', 'rb')
# data2 = file2.read()
# print(data2)
# values1 = struct.unpack('>i4sh', data2)
# print(values1)

with open('myfile.txt', 'rb') as myfile:
    for line in myfile:
        print("myfile.txt：", line)

myfile1 = open('myfile.txt', 'r')
try:
    for line in myfile1:
        print("myfile.txt（using try finally）：", line)
finally:
    myfile1.close()

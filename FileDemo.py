__author__ = 'huangw-d'
myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goobye text file\n')
myfile.close()  # Flush output buffers to disk

myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())

data = open('myfile.txt', 'rb').read()  # 以二进制数据读取文件内容
print(data)

x, y, z = 43, 44, 45
s = 'spam'
d = {'a': 1, 'b': 2}
l = [1, 2, 3]
f = open('datafile.txt', 'w')
f.write(s + '\n')
f.write('%s,%s,%s\n' % (x, y, z))
f.write(str(l) + '$' + str(d) + '\n')
f.close()
for line in open('datafile.txt'):
    print(line, end='')  # 二进制文件读取
    dllData = open('e:\System.Text.RegularExpressions.dll', 'rb').read()
    print(dllData[4:8])
    print(dllData[0])
    print(bin(dllData[0]))

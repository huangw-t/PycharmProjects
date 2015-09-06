__author__ = 'huangw-d'
# 字典比较
# Python2.6和更早的版本中
D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(D1 == D2)
# print(D1 < D2)

# Python3.0之后，字典不再支持直接比较
D3 = {'a': 1, 'b': 2}
D4 = {'a': 1, 'b': 3}
print("list(D3.items():)", list(D3.items()))
print("sorted(D3.items():)", sorted(D3.items()))
print("list(D4.items():)", list(D4.items()))
print("sorted(D4.items():)", sorted(D4.items()))
print("sorted(D3.items())< sorted(D4.items()):", sorted(D3.items()) < sorted(D4.items()))
print("sorted(D3.items())> sorted(D4.items()):", sorted(D3.items()) > sorted(D4.items()))

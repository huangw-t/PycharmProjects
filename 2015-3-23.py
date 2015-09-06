__author__ = 'huangw-d'
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
dictUnion = {'a': 1, 'b': 2, 'c': 3}
print(dictUnion.keys() & dictUnion.keys())
print(dictUnion.keys() & {'b'})
print(dictUnion.keys() & {'b': 1})
print(dictUnion.keys() | {'b', 'c', 'd'})

dictHash = {'a': 1}
print('dictHash items:', list(dictHash.items()))
print("union view and view:", dictHash.items() | dictHash.keys())
print('dict treated same as its key:', dictHash.items() | dictHash)
print('set of key/values pairs:', dictHash.items() | {('c', 3), ('d', 4)})
print('dict accepts iterable sets too:', dict(dictHash.items() | {('c', 3), ('d', 4)}))

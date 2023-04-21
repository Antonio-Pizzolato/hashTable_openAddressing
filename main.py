# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import array as arr
import random
import time
import numpy as np

# elements = [int(item) for item in
#             input("Enter the elements which are going to be inserted in the hash table: ").split()]
# print(elements)
#
# elements_number = len(elements)
# print('Number of elements: ', elements_number)


elements_number = int(input("Enter the length of the array that will be randomly created: "))
elements = np.random.randint(0, 9999, elements_number)
print(elements)

# linear hash function (non solo con coefficiente 1)
def linearHash(x, i):
    h1 = (x - (round(x / elements_number,
                     0) * elements_number))  # la funzione round(a, b) arrotonda il numero a con k cifre decimale ad un numero a con b cifre decimali (in questo caso approssimazione intera per difetto)
    x = (h1 + (1 * i)) - (round((h1 + (1 * i)) / elements_number, 0) * elements_number)
    return x


# quadratic hash function
def quadraticHash(x, i):
    h1 = (x - (round(x / elements_number, 0) * elements_number))
    x = (h1 + ((1 / 2) * i) + ((1 / 2) * pow(i, 2))) - (
            round((h1 + ((1 / 2) * i) + ((1 / 2) * pow(i, 2))) / elements_number, 0) * elements_number)
    return x


# double hash function
def doubleHash(x, i):
    h1 = (x - (round(x / elements_number, 0) * elements_number))
    h2 = 1 + (x - (round(x / (elements_number - 1), 0) * (elements_number - 1)))
    x = ((h1 + (i * h2)) - (round((h1 + (i * h2)) / elements_number, 0) * elements_number))
    return x


function = int(
    input('Choose what function to use (insert the number): \n1. linear hash \n2. quadratic hash \n3. double hash\n'))
if function == 1:
    HashFunction = linearHash
elif function == 2:
    HashFunction = quadraticHash
elif function == 3:
    HashFunction = doubleHash


class HashTable(object):
    default_size = int(input('Type the default size of the hash table: '))
    # table = [default_size]
    empty_cell = None
    deleted_cell = None
    table = [empty_cell] * default_size
    load_factor = elements_number / default_size  # in realtà elements_number dovrebbe essere sostituito con il numero di elementi inseriti nella tabella/cella, elements_number è il numero di elementi che DOVREBBERO essere inseriti nella tabella

    def insert(T, value):
        i = 0
        while True:
            k = int(HashFunction(value, i))
            # if k >= elements_number:
            #     print("Error")
            #     return
            if HashTable.table[k] == HashTable.empty_cell or HashTable.deleted_cell:
                HashTable.table[k] = value
                return k
            else:
                i = i + 1
            if i >= HashTable.default_size:
                print("Error: Hash Table Overflow")
                return

    def search(T, value):
        i = 0
        while True:
            k = int(HashFunction(value, i))
            if HashTable.table[k] == value:
                return k
            i = i + 1
            if HashTable.table[k] == HashTable.empty_cell or i == HashTable.default_size:  # con una deleted_cell la ricerca deve continuare
                print('ERROR: value not found')
                return

    def delete(T, value):
        i = 0
        while i < HashTable.default_size:
            k = int(HashFunction(value, i))
            if HashTable.table[k] == HashTable.empty_cell or HashTable.table[k] == HashTable.deleted_cell:
                return
            if HashTable.table[k] == value:
                HashTable.table[k] = HashTable.deleted_cell
                return
            i = i + 1


T = HashTable()
elements = arr.array('i', elements)

start = time.perf_counter()
for element in elements:
    HashTable.insert(T, element)
end = time.perf_counter()

print('\n', 'Hash Table: ', T.table)
print('Time in seconds to insert elements into the Hash Table: '"%10.10f" % (end - start), '\n')

searched = int(input("Insert the value you are looking for in the hash table: "))
start = time.perf_counter()
a = HashTable.search(T, searched)
end = time.perf_counter()
print('Index of the searched element: ', a)
print('Time in seconds to look for the element into the Hash Table: '"%10.10f" % (end - start), '\n')

deleted = int(input("Insert the value you want to delete in the hash table: "))
start = time.perf_counter()
HashTable.delete(T, deleted)
end = time.perf_counter()
print('Hash Table with deleted element: ', T.table)
print('Time in seconds to delete the element into the Hash Table: '"%10.10f" % (end - start))

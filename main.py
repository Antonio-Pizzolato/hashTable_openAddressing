# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# NOTA: forse conviene spostare tutte le funzioni insert, ecc. in HashTable (dato che sono comuni a tutte le funzioni hash open addressing)
import array as arr
import time

elements = [int(item) for item in input("Enter the elements which are going to be inserted in the hash table: ").split()]
print(elements)

elements_number = len(elements)
print('Number of elements: ', elements_number)


class HashTable(object):
    default_size = int(input('Type the default size of the hash table: '))
    #table = [default_size]
    empty_cell = None
    deleted_cell = None
    table = [empty_cell] * default_size
    load_factor = elements_number / default_size  # in realtà elements_number dovrebbe essere sostituito con il numero di elementi inseriti nella tabella/cella, elements_number è il numero di elementi che DOVREBBERO essere inseriti nella tabella

    # linear hash function
    def linearHash(x, i):
        h1 = (x - (round(x / elements_number, 0) * elements_number))  # la funzione round(a, b) arrotonda il numero a con k cifre decimale ad un numero a con b cifre decimali (in questo caso approssimazione intera per difetto)
        x = (h1 + i) - (round((h1 + i) / elements_number, 0) * elements_number)
        return x

    # quadratic hash function
    def quadraticHash(x, i):
        h1 = (x - (round(x / elements_number, 0) * elements_number))
        x = (h1 + ((1/2) * i) + ((1/2) * pow(i, 2))) - (round((h1 + ((1/2) * i) + ((1/2) * pow(i, 2))) / elements_number, 0) * elements_number)
        return x

    # double hash function
    def doubleHash(x, i):
        h1 = (x - (round(x / elements_number, 0) * elements_number))
        h2 = 1 + (x - (round(x / (elements_number - 1), 0) * (elements_number - 1)))
        x = ((h1 + (i * h2)) - (round((h1 + (i * h2)) / elements_number, 0) * elements_number))
        return x

    def insert(T, value):
        i = 0
        while True:
            k = int(HashTable.doubleHash(value, i))
            if HashTable.table[k] == HashTable.empty_cell or HashTable.deleted_cell:
                HashTable.table[k] = value
                return k
            else:
                i = i + 1
            if i == HashTable.default_size:
                print("Error: Hash Table Overflow")
                return

    def search(T, value):
        i = 0
        while True:
            k = int(HashTable.linearHash(value, i))
            if HashTable.table[k] == value:
                return k
            i = i + 1
            if HashTable.table[k] == HashTable.empty_cell or i == HashTable.default_size:  # con una deleted_cell la ricerca deve continuare
                print('ERROR: value not found')
                return

    def delete(T, value):
        i = 0
        while i < HashTable.default_size:
            k = int(HashTable.linearHash(value, i))
            if HashTable.table[k] == HashTable.empty_cell or HashTable.table[k] == HashTable.deleted_cell:
                return
            if HashTable.table[k] == value:
                HashTable.table[k] = HashTable.deleted_cell
                return
            i = i + 1


T = HashTable()
elements = arr.array('i', elements)
print(elements)

start = time.time()
for element in elements:
    HashTable.insert(T, element)
end = time.time()
print("%10.10f" % (end-start))

print(T.table)

a = HashTable.search(T, 2)
print(a)

HashTable.delete(T, 2)
print(T.table)

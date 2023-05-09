import array as arr
import time
import numpy as np
import matplotlib.pyplot as plt

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
    empty_cell = None
    deleted_cell = None
    table = [empty_cell] * default_size
    load_factor = elements_number / default_size  # in realtà elements_number dovrebbe essere sostituito con il numero di elementi inseriti nella tabella/cella, elements_number è il numero di elementi che DOVREBBERO essere inseriti nella tabella

    def insert(T, value):
        i = 0
        while True:
            k = int(HashFunction(value, i))
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
        start_s = time.perf_counter()
        time_array_search = [0.0] * T.default_size
        n_s = 0
        while True:
            k = int(HashFunction(value, i))
            if HashTable.table[k] == value:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                return k, time_array_search
            i = i + 1
            if HashTable.table[
                k] == HashTable.empty_cell or i == HashTable.default_size:  # con una deleted_cell la ricerca deve continuare
                print('ERROR: value not found')
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                return time_array_search
            end_s = time.perf_counter()
            time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
            n_s = n_s + 1

    def delete(T, value):
        i = 0
        start_d = time.perf_counter()
        time_array_delete = [0.0] * T.default_size
        n_d = 0
        while i < HashTable.default_size:
            k = int(HashFunction(value, i))
            if HashTable.table[k] == HashTable.empty_cell or HashTable.table[k] == HashTable.deleted_cell:
                end_d = time.perf_counter()
                time_array_delete[n_d] = round(time_array_delete[n_d - 1] + ((end_d - start_d) * 1000), 4)
                print("ERROR: value not found")
                return time_array_delete
            elif HashTable.table[k] == value:
                HashTable.table[k] = HashTable.deleted_cell
                end_d = time.perf_counter()
                time_array_delete[n_d] = round(time_array_delete[n_d - 1] + ((end_d - start_d) * 1000), 4)
                return time_array_delete
            i = i + 1
            end_d = time.perf_counter()
            time_array_delete[n_d] = round(time_array_delete[n_d - 1] + ((end_d - start_d) * 1000), 4)
            n_d = n_d + 1
        print("ERROR: value not found")
        return time_array_delete


T = HashTable()
elements = arr.array('i', elements)

start = time.perf_counter()
n = 0
time_array_insert = [0.0] * T.default_size
for element in elements:
    HashTable.insert(T, element)
    end = time.perf_counter()
    time_array_insert[n] = round(time_array_insert[n - 1] + ((end - start) * 1000), 4)
    n = n + 1

print('\n', 'Hash Table: ', T.table)
print('\n', 'Insert Time: ', time_array_insert)

searched = int(input("Insert the value you are looking for in the hash table: "))
time_search = HashTable.search(T, searched)
print('Search Time: ', time_search)

deleted = int(input("Insert the value you want to delete in the hash table: "))
time_delete = HashTable.delete(T, deleted)
print('Hash Table with deleted element: ', T.table)
print('Delete Time: ', time_delete)

number_of_elements_arr = [0.0] * T.default_size
x = 0
while x < T.default_size:
    number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    x = x + 1

plt.title("Inserimento")
plt.xlabel("numero di elementi da ordinare")
#plt.xticks(number_of_elements_arr, number_of_elements_arr)
plt.ylabel("tempo in millisecondi")
#plt.yticks(time_array_insert, time_array_insert)
plt.plot(number_of_elements_arr, time_array_insert)
plt.show()

plt.title("Ricerca")
plt.xlabel("numero di elementi da ordinare")
#plt.xticks(number_of_elements_arr, number_of_elements_arr)
plt.ylabel("tempo in millisecondi")
#plt.yticks(time_search, time_search)
plt.plot(number_of_elements_arr, time_search)
plt.show()

plt.title("Cancellazione")
plt.xlabel("numero di elementi da ordinare")
#plt.xticks(number_of_elements_arr, number_of_elements_arr)
plt.ylabel("tempo in millisecondi")
#plt.yticks(time_delete, time_delete)
plt.plot(number_of_elements_arr, time_delete)
plt.show()

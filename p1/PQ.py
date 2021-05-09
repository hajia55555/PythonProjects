#Implementing a priority queue with a Max-Binary Heap
#Adding a integer key into a Binary Heap that points to a value in a dictionary

#Insert a key into a heap
#Inserts its (key,value) pair into a dictionary
def Insert(heap, key, value):
    heap.append(key)
    dict[key] = value


def heapify(heap, heapsize, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < heapsize and heap[l] > heap[largest]:
        largest = l

    if r < heapsize and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, heapsize, largest)


#Returning maximum element from heap
def Maximum(heap):
    n = len(heap)

    for i in range(n//2 - 1, -1, -1):
        heapify(heap, n, i)
    
    max = heap[0]
    return dict[max]

#delete an element from the heap
def Extract_Max(heap):
    n = len(heap) - 1
    Maximum(heap)

    max = heap[0]

    heap[0] = heap[n]
    heap.pop(n)
    heapify(heap, n, 1)
    
    return dict[max]

heap = []
dict = {}


file1 = open("input.txt",'r')
file2 = open("output.txt", 'w')
for line in file1:
    line = line.split()
    if line[0] == 'insert':
        Insert(heap, int(line[2]), line[1])
    elif line[0] == 'max':
        file2.write(Maximum(heap) + "\n")
    elif line[0] == 'extract':
        Extract_Max(heap)
    elif line[0] == 'quit':
        while heap:
            file2.write(Extract_Max(heap) + " ")
        

file1.close()
file2.close()

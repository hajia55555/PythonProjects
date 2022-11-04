# Implementing a priority queue with a Max-Binary Heap
# Adding a integer key into a Binary Heap that points to a value in a dictionary

# Insert a key into a heap
# Inserts its (key,value) pair into a dictionary
def Insert(heap, key, value):
    heap.append(key)
    dict[key] = value


# Sorting the list "heap" 
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


# Creating the Max-Heap
def BuildMaxHeap(heap):
    n = len(heap)

    for i in range(n//2 - 1, -1, -1):
        heapify(heap, n, i)


# Returning maximum element from queue
def Maximum(heap):    
    max = heap[0]
    return dict[max]


# Delete the value in the front of the queue (heap)
def Extract_Max(heap):
    n = len(heap) - 1
    BuildMaxHeap(heap)

    max = heap[0]

    heap[0] = heap[n]
    heap.pop(n)
    heapify(heap, n, 1)
    
    return dict[max]


heap = []
dict = {}


inputFile = open("input.txt",'r')
outputFile = open("output.txt", 'w')

for line in inputFile:
    line = line.split()
    if line[0] == 'insert':
        Insert(heap, int(line[2]), line[1])
    elif line[0] == 'max':
        BuildMaxHeap(heap)
        outputFile.write(Maximum(heap) + "\n")
    elif line[0] == 'pop':
        Extract_Max(heap)
    elif line[0] == 'quit':
        while heap:
            outputFile.write(Extract_Max(heap) + " ")
        outputFile.write("\n")   


inputFile.close()
outputFile.close()

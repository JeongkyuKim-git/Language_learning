import queue

"""
일반적인 Queue (First-In, First-Out)
"""

# value | data_queue
# value_box | Queue()
data_queue = queue.Queue()

# data insert | put(data)
data_queue.put(1)

# data size check | qsize()
print(data_queue.qsize())

# data delete or output | get()
print(data_queue.get())

# ---------------------------

"""
LifoQueue() (LIFO(Last-In, First-Out))
"""
# value | data_queue_02
# value_box | LifoQueue()
data_queue_02 = queue.LifoQueue()

data_queue_02.put(1)
data_queue_02.put(3)
data_queue_02.put(5)

print(data_queue_02.get())
print("01 get")
print(data_queue_02.get())
print("02 get")
print(data_queue_02.get())
print("03 get")

# ---------------------------------

"""
PriorityQueue() 우선순위 queue
"""
# value | data_queue_03
# value_box | PriorityQueue()
data_queue_03 = queue.PriorityQueue()

# put((우선순위 번호, 데이터))
data_queue_03.put((3, "C"))
data_queue_03.put((10, "G"))
data_queue_03.put((1, "A"))

print(data_queue_03.qsize())

print(data_queue_03.get())

# -----------------------------------
# import queue 를 사용하지 않고 코드 작성

print("clear ----------------------")
queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

print(len(queue_list))

print(dequeue())
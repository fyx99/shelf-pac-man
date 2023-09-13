import queue

def my_generator():
    a = 1

def enqueue_values_to_queue(generator, q):
    for value in generator:
        q.put(value)

# Create a queue
my_queue = queue.Queue()

# Create the generator
gen = my_generator()

# Enqueue yielded values into the queue
enqueue_values_to_queue(gen, my_queue)

# Now the queue contains the values yielded by the generator
while not my_queue.empty():
    value = my_queue.get()
    print(value)
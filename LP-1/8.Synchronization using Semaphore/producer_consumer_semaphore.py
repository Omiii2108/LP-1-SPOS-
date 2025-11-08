# Classical Synchronization Problem: Producer–Consumer using Semaphores
import threading
import time
import random

# Shared buffer
buffer = []
BUFFER_SIZE = 5  # Maximum items in buffer

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Counts empty slots
full = threading.Semaphore(0)             # Counts filled slots
mutex = threading.Semaphore(1)            # Mutual exclusion lock

MAX_PRODUCE = 10  # Limit to stop program

def producer():
    for i in range(MAX_PRODUCE):
        time.sleep(random.uniform(0.5, 1.5))  # Simulate production time
        item = f"Item-{i+1}"

        empty.acquire()    # Wait for an empty slot
        mutex.acquire()    # Lock buffer access

        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")

        mutex.release()
        full.release()     # Signal that a new item is available

    print("\nProducer finished producing.\n")

def consumer():
    for i in range(MAX_PRODUCE):
        full.acquire()     # Wait for available item
        mutex.acquire()    # Lock buffer access

        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")

        mutex.release()
        empty.release()    # Signal that a slot is empty

        time.sleep(random.uniform(0.5, 1.5))  # Simulate consumption time

    print("\nConsumer finished consuming.\n")

if __name__ == "__main__":
    print("=== Producer–Consumer Problem using Semaphores ===\n")

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("✅ Program completed successfully.")

# Reader–Writer Problem using Mutex (Finite Version)

import threading
import time
import random

# Shared resource
data = 0

# Mutex locks
read_lock = threading.Lock()
write_lock = threading.Lock()

reader_count = 0
MAX_WRITES = 5  # Program will stop after 5 writes
write_done = False

def reader(reader_id):
    global reader_count, write_done
    while not write_done:
        time.sleep(random.uniform(0.5, 1.5))

        # Entry section for reader
        read_lock.acquire()
        reader_count += 1
        if reader_count == 1:
            write_lock.acquire()
        read_lock.release()

        # Critical section (reading)
        print(f"Reader {reader_id} is reading data = {data}")
        time.sleep(random.uniform(0.3, 0.7))

        # Exit section for reader
        read_lock.acquire()
        reader_count -= 1
        if reader_count == 0:
            write_lock.release()
        read_lock.release()

def writer(writer_id):
    global data, write_done
    for i in range(MAX_WRITES):
        time.sleep(random.uniform(1, 2))
        write_lock.acquire()
        data += 1
        print(f"Writer {writer_id} wrote data = {data}")
        write_lock.release()
    write_done = True  # Signal readers to stop

if __name__ == "__main__":
    print("=== Reader–Writer Problem using Mutex (Auto Stop Version) ===\n")

    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(1)]

    for t in readers + writers:
        t.start()

    for t in readers + writers:
        t.join()

    print("\n✅ Program completed successfully.")

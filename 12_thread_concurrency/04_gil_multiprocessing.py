from multiprocessing import Process
import time

def crunch_numbers():
    print("Started the count process")
    count = 0
    for _ in range(100_000_000):
      count += 1
    print("End the count process")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_numbers)
    p2 = Process(target=crunch_numbers)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-procesing is: {end-start:.2f} seconds")

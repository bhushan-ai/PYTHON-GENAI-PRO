from multiprocessing import Process
import time 

def cpu_heavy():
    print("Crunching the numbers...")
    total = 0
    for i in range(10**8):
        total+=i
    print("Done ✅")

start = time.time()

if __name__ == "__main__":
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Time taken: {time.time() - start:.2f} secs")
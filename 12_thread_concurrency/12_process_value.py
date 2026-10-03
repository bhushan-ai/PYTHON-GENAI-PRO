from multiprocessing import Process, Queue, Value

def increment(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value+=1

# there are 4 processes goin on when 1st process is reach it will get its own lock, and when other process is reach it will just get the value and keep on incrementing it, each process is able to share its value
if __name__ == "__main__":
    counter = Value("i", 0)
    procesess = [Process(target=increment, args=(counter, )) for _ in range(4)] 
    [p.start() for p in procesess]
    [p.join() for p in procesess]
    print(f"Final counter value {counter.value}")

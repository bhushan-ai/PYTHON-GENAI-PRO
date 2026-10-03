from multiprocessing import Process, Queue, Value

def prepare_chai(queue):
    queue.put("Masala chai is ready")


if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=prepare_chai,args=(queue, ))
    p1.start()
    p1.join()

    print(queue.get())
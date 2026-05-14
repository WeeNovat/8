import queue

def producer(q: queue.Queue):
    for i in range(5):
        q.put(f"Задача #{i}")
        time.sleep(0.1)
    q.put(None) 

def consumer(q: queue.Queue):
    while True:
        task = q.get()
        if task is None: break
        print(f"Оброблено: {task}")
        q.task_done()

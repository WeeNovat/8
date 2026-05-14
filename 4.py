class ConnectionPool:
    def __init__(self, max_conn=3):
        self._sem = threading.Semaphore(max_conn)
        self.active_connections = 0
        self._lock = threading.Lock()

    def acquire(self, name):
        self._sem.acquire()
        with self._lock: self.active_connections += 1
        print(f"[{name}] З'єднано. Активних: {self.active_connections}")

    def release(self, name):
        with self._lock: self.active_connections -= 1
        self._sem.release()
        print(f"[{name}] Від'єднано.")

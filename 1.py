import threading
import time

def download_simulation(file_name: str, size_mb: float) -> dict:
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] Початок завантаження '{file_name}' ({size_mb} MB)...")
    time.sleep(size_mb * 0.5)  
    print(f"[{thread_name}] '{file_name}' готово!")
    return {"file": file_name, "size": size_mb, "thread": thread_name}

class MonitorThread(threading.Thread):
    def __init__(self, interval: float = 1.0):
        super().__init__(name="Monitor", daemon=True)
        self.interval = interval
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            print(f"\n[MONITOR] Активних потоків: {threading.active_count()}")
            time.sleep(self.interval)

def main():
    files = [("data.csv", 2.0), ("report.pdf", 1.0), ("image.png", 0.5), ("arch.zip", 3.0)]
    monitor = MonitorThread(0.8)
    monitor.start()

    start = time.perf_counter()
    threads = []
    for name, size in files:
        t = threading.Thread(target=download_simulation, args=(name, size))
        threads.append(t)
        t.start()

    for t in threads: t.join()
    monitor.stop()

    parallel_time = time.perf_counter() - start
    seq_time = sum(f[1] * 0.5 for f in files)
    print(f"\nПаралельно: {parallel_time:.2f}с | Послідовно: {seq_time:.2f}с")
    print(f"Прискорення: {seq_time / parallel_time:.2f}x")

if __name__ == "__main__": main()

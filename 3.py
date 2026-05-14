import threading
import time

class SafeBankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        self._lock = threading.Lock()

    def deposit(self, amount: float):
        with self._lock:
            curr = self.balance
            time.sleep(0.0001) 
            self.balance = curr + amount

    def withdraw(self, amount: float):
        with self._lock:
            if self.balance >= amount:
                curr = self.balance
                time.sleep(0.0001)
                self.balance = curr - amount

def main():
    acc = SafeBankAccount(1000.0)
    threads = []
    for _ in range(50):
        threads.append(threading.Thread(target=acc.deposit, args=(10.0,)))
        threads.append(threading.Thread(target=acc.withdraw, args=(10.0,)))

    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Фінальний баланс: {acc.balance} (Очікувано: 1000.0)")

if __name__ == "__main__": main()

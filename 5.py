from concurrent.futures import ThreadPoolExecutor, as_completed

def risky_task(n):
    if n == 0: raise ZeroDivisionError("Спроба ділення на нуль!")
    return 100 / n

def handle_exceptions():
    values = [10, 0, 5, -1]
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(risky_task, v): v for v in values}
        for future in as_completed(futures):
            try:
                print(f"Результат для {futures[future]}: {future.result()}")
            except Exception as e:
                print(f"Помилка для {futures[future]}: {e}")

if __name__ == "__main__": handle_exceptions()

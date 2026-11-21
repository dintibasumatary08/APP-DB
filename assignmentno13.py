import threading
import time
import random

results = {}
lock = threading.Lock()


def compute_squares(n):
    total = sum(i * i for i in range(1, n + 1))
    with lock:
        results["sum_of_squares"] = total
    print(f"[{threading.current_thread().name}] Sum of squares up to {n} = {total}")


def count_primes(limit):
    count = 0
    for num in range(2, limit + 1):
        if all(num % d for d in range(2, int(num ** 0.5) + 1)):
            count += 1
    with lock:
        results["prime_count"] = count
    print(f"[{threading.current_thread().name}] Primes up to {limit} = {count}")


def simulate_download(file_name):
    print(f"[{threading.current_thread().name}] Downloading {file_name}...")
    time.sleep(random.uniform(0.5, 2))
    with lock:
        results[file_name] = "completed"
    print(f"[{threading.current_thread().name}] Finished {file_name}")


def print_heartbeat(text, times):
    for i in range(1, times + 1):
        print(f"[{threading.current_thread().name}] {text} {i}/{times}")
        time.sleep(0.3)


if __name__ == "__main__":
    tasks = [
        threading.Thread(target=compute_squares, args=(10000,), name="Thread-Squares"),
        threading.Thread(target=count_primes, args=(50000,), name="Thread-Primes"),
        threading.Thread(target=simulate_download, args=("report.pdf",), name="Thread-Download"),
        threading.Thread(target=print_heartbeat, args=("Heartbeat", 4), name="Thread-Heartbeat"),
    ]

    start = time.time()
    for t in tasks:
        t.start()
    for t in tasks:
        t.join()

    print(f"\nAll threads finished in {time.time() - start:.2f} seconds")
    print("Results:", results)
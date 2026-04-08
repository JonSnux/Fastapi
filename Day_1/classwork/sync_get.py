import requests
import time

def read_example() -> None:
    response = requests.get("https://example.com")
    print("Status code:", response.status_code)

sync_start = time.perf_counter()
read_example()
read_example()
sync_end = time.perf_counter()

print(f"Выполнение кода заняло: {sync_end - sync_start:.4f} c.")
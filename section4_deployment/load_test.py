import time
import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8000/chat"

payload = {
    "question": "What is the return policy?"
}

times = []


def send_request(i):
    start = time.perf_counter()

    response = requests.post(URL, json=payload)

    elapsed = time.perf_counter() - start
    times.append(elapsed)

    print(
        f"Request {i+1}: "
        f"{elapsed:.2f} sec | "
        f"Status={response.status_code}"
    )


if __name__ == "__main__":

    print("Sending 10 concurrent requests...\n")

    total_start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(send_request, range(10))

    total_time = time.perf_counter() - total_start

    print("\n---------- Results ----------")
    print(f"Requests      : {len(times)}")
    print(f"Average Time  : {sum(times)/len(times):.2f} sec")
    print(f"Fastest       : {min(times):.2f} sec")
    print(f"Slowest       : {max(times):.2f} sec")
    print(f"Total Time    : {total_time:.2f} sec")
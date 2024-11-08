# ThreadPoolExecutor - it is a class that is used to create a thread pool executor

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


# it is IO bound task (input/output)
def get_url(url):
    response = requests.get(url)
    return response.status_code


# CPU bound task (DONT USE THREADING FOR CPU BOUND TASKS)
def cpu_bound_task(url):
    x = 0
    for i in range(1_000_000):
        x += 1
    return x


def single_thread(urls):
    for url in urls:
        print(get_url(url))


def multi_thread(urls):
    threads = []
    for url in urls:
        t = threading.Thread(target=get_url, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


def thread_pool_executor(urls):
    with ThreadPoolExecutor() as executor:
        results = executor.map(get_url, urls)
        for result in results:
            print(result)


def main():
    urls = ["https://www.google.com", "https://www.yahoo.com", "https://www.bing.com"]
    # single_thread(urls)  # 2.7 seconds for 3 urls
    # multi_thread(urls)  # 1.4 seconds for 3 urls
    thread_pool_executor(urls)  # 0.9 seconds for 3 urls


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Time used: {end - start}")

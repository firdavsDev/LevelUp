"""
Python Multiprocessing Module

The multiprocessing module allows you to create separate processes, each of them running in its own instance of the Python interpreter. This means that each process has its own memory space, so an object in one process is not accessible in another process.
"""

import multiprocessing
import time

file_name = "words.txt"
the_word = "qwertyuiopasdfghjklzxcvbnm"


def writes():
    with open(file_name, "a") as file:
        for _ in range(1_000_000):
            file.write(f"{the_word}\n")


def clear():
    # delete line by line for 10_000_000 times
    with open(file_name, "a+") as file:
        for _ in range(1_000_000):
            file.write("1")


def reads():
    with open(file_name, "r") as file:
        lines = file.readlines()
    return len(lines)


def sleeper(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Done sleeping...")


if __name__ == "__main__":
    start = time.perf_counter()
    # p1 = multiprocessing.Process(target=writes)
    # p1.start()
    # p1.join()
    # p2 = multiprocessing.Process(target=clear)
    # p2.start()
    # p2.join()
    p3 = multiprocessing.Process(target=sleeper, args=[100], name="sleeper")
    p3.start()
    print(f"Process ID: {p3.pid}")
    print(f"Process Name: {p3.name}")
    p3.join()

    end = time.perf_counter()
    print(f"Time used: {end - start}")


x = 6
y = 7
print(y)

# print x reference count
import sys

print(sys.getrefcount(y))  # it returns 2 because x is referenced twice in the code
print(
    sys.getrefcount(x)
)  # it returns 3 because x is referenced twice in the code and once in the sys.getrefcount function

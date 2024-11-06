"""
Python GIL is a mutex that allows only one thread to hold the control of the Python interpreter.
This means that only one thread can be in a state of execution at any point in time.
This simplifies the CPython implementation by making the object model inherently thread-safe.
However, the GIL makes multi-threaded programming more difficult in Python because the majority of the threads cannot run in parallel.
This is because they are blocked by the GIL.
The GIL is necessary mainly because CPython’s memory management is not thread-safe.
The GIL exists even though most modern processors have multiple cores.

"""

# import threading
# import time


# # Example 2 Increasing variable value using threads and GIL in Python

# INCREMENT_NUMBER = 1_000_000
# X = 0


# def increment_with_gil():
#     for i in range(0, 1_000_000):
#         global X
#         X += 1


# def main():
#     print(f"Starting value of X: {X}")
#     t1 = threading.Thread(target=increment_with_gil)
#     t2 = threading.Thread(target=increment_with_gil)

#     # starting threads
#     t1.start()
#     t2.start()

#     # wait until threads finish their job
#     t1.join()
#     t2.join()
#     print("------------------- Thread finished -------------------")
#     print(f"Finished value of X: {X}")


# if __name__ == "__main__":
#     main()

# TASK: Write 10_000_000 line text to a 2 files using threads and GIL in Python
# 1) Create a function that clears the content of a file
# 2) Create a function that writes a text to a file
# 3) Create a function that reads the content of a file

import threading
import time


############ Example 1 ############

# def print_numbers():
#     for i in range(100):
#         print(i)


# t1 = threading.Thread(target=print_numbers, name="task_1")
# # set the thread as a daemon thread
# t1.setDaemon(
#     True
# )  # The main thread will not wait for the daemon thread to finish. If the main thread finishes before the daemon thread, the daemon thread will not die and will continue to run in the background.

# t1.start()  # Start the thread
# # t1.join()  # Wait for the thread to finish
# print("Thread finished")


# print(f"{t1.getName()} is alive:, {t1.is_alive()}")


# Main thread will wait for the t1 thread to finish before printing 'Thread finished'

############ Example 2 ############

# def work_after_n_seconds(n):
#     print(f"Sleeping for {n} seconds")
#     time.sleep(n)
#     print("Done sleeping")


# t2 = threading.Thread(target=work_after_n_seconds, args=(150,), name="task_2")
# t2.setDaemon(True)
# t2.start()
# # t2.join()
# print("Thread finished")
# print(f"{t2.getName()} is alive:, {t2.is_alive()}")

############ Example 3 ############
COUNT = 10_000_000


def countdown(n):
    while n > 0:
        n -= 1


start = time.perf_counter()
# countdown(COUNT)
# countdown(COUNT)
# 0.41 seconds for 2 times calling the function
t1 = threading.Thread(target=countdown, args=(COUNT,))
t2 = threading.Thread(target=countdown, args=(COUNT,))
t1.start()
t2.start()
# t1.join()
# t2.join()
end = time.perf_counter()

# prin time taken in seconds format
print(f"Time taken in seconds - {end-start}")

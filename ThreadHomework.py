# TASK: Write 10_000_000 line text to a 2 files using threads and GIL in Python
# 1) Create a function that clears the content of a file
# 2) Create a function that writes a text to a file
# 3) Create a function that reads the content of a file
import threading
import time


the_word = "qwertyuiopasdfghjklzxcvbnm"
file_name = 'words.txt'


def writes():
    with open (file_name, 'a') as file:
        for item in range(9_999):
            file.write(f"{the_word}\n")
        file.write(the_word)



def clears():
    a = 10_000
    while a != 0:
        with open (file_name, 'w') as file:
            file.writelines(lines[:-1])
        a -= 1


def reads():
    with open (file_name, 'r') as file:
        lines = file.readlines()
    return len(lines)


def main():
    start = time.perf_counter()
    t1 = threading.Thread(target=writes(), name="yozuvchi")
    t2 = threading.Thread(target=clears(), nmae="tozalovchi")
    t1.start()
    t2.start()
    end = time.perf_counter()
    print(t1.getName())
    print(t2.getName())
    print(f"The number of rows remaining {reads()}")
    print(f"Time used: {start - end}")


if __name__=="__main__":
    main()
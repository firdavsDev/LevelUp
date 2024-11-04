from my_logger import logging

# DEBUG
print(logging.DEBUG)  # 10 # when you want to know what's going on in your program
# INFO
print(logging.INFO)  # 20 # when something expected happens (user logs in)
# WARNING
print(
    logging.WARNING
)  # 30 # when something unexpected happens (1 000 000$ transaction)
# ERROR
print(logging.ERROR)  # 40 # when your program runs into a problem (try/except)
# CRITICAL
print(logging.CRITICAL)  # 50 when your program crashes


def error_handling(a: int, b: int):
    logging.debug("This is a debug message")
    try:
        logging.info(f"a is {a}, b is {b}")
        div = a / b
        logging.info(f"Division is {div}")
        return div
    except Exception as e:
        logging.error(f"Exception occurred: {e}")


if __name__ == "__main__":
    error_handling(5, 0)


@my_custom_loger  # home task
def error_handling(a: int, b: int):
    div = a / b
    return div

from my_logger import logging

# # DEBUG
# print(logging.DEBUG)  # 10 # when you want to know what's going on in your program
# # INFO
# print(logging.INFO)  # 20 # when something expected happens (user logs in)
# # WARNING
# print(
#     logging.WARNING
# )  # 30 # when something unexpected happens (1 000 000$ transaction)
# # ERROR
# print(logging.ERROR)  # 40 # when your program runs into a problem (try/except)
# # CRITICAL
# print(logging.CRITICAL)  # 50 when your program crashes


# def error_handling(a: int, b: int):
#     logging.debug("This is a debug message")
#     try:
#         logging.info(f"a is {a}, b is {b}")
#         div = a / b
#         logging.info(f"Division is {div}")
#         return div
#     except Exception as e:
#         logging.error(f"Exception occurred: {e}")

################################################## home work ######################################################

def my_custom_logger(original_func):
    def error_func(*args, **kwargs):
        logging.debug("ishga tushdi")
        try:
            print("1")
            logging.info(f"o'zgaruvchilar: a = {args[0]}, b = {args[1]}")
            new_value = original_func(*args, **kwargs)
            logging.info(f"xatoliksiz ishlayabdi")
            return new_value
        except Exception as e:
            logging.warning("xatolik chiqdi")
            logging.error(f"Xatolik: {e}")
    return error_func


@my_custom_logger  # home task
def error_handling(a: int, b: int):
    div = a / b
    return div


if __name__ == "__main__":
    error_handling(5, 0)
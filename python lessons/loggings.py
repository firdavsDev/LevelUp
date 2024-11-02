import logging
import logging.config

# LOGGING LEVELS
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"

# logging.basicConfig(filename="example.log", level=logging.DEBUG)
logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format=fmtStr,
    datefmt="%m/%d/%Y %I:%M:%S %p",
    style="%",
)


def error_function():
    try:
        logging.info("Function started")
        print(1 / 0)
    except Exception as e:
        logging.error("An error occured")


if __name__ == "__main__":
    error_function()

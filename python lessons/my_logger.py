import logging

# Must be called top on the file
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s:Line: %(lineno)d",
)

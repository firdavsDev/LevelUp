"""
decorator'lar nima?
- Decorator'lar, bir fonksiyonu değiştirmek için kullanılan bir tasarım desenidir.
"""


def decorator_func(original_func):

    def wrapper_func(*args, **kwargs):
        print("wrapper executed this before {}".format(original_func.__name__))
        new_value = original_func(*args, **kwargs)
        new_value = f"{new_value} aka"
        print(new_value)
        return new_value

    return wrapper_func


@decorator_func
def display(name):
    return f"Hello {name}"


def my_handler(original_func):

    def wrapper_func(*args, **kwargs):
        try:
            new_value = original_func(*args, **kwargs)
            return new_value
        except Exception as e:
            print(f"Error: {e}")

    return wrapper_func


@my_handler
def error_func():
    return 1 / 0


def my_timer(original_func):

    from time import perf_counter

    def wrapper_func(*args, **kwargs):
        t1 = perf_counter()
        result = original_func(*args, **kwargs)
        t2 = perf_counter() - t1
        print(f"{original_func.__name__} ran in: {t2} sec")
        return result

    return wrapper_func


@my_timer
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


@my_timer
def find_even_numbers():
    numbers = [x for x in range(10_000)]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


if __name__ == "__main__":
    # decorated_display = decorator_func(display)
    # decorated_display('John Doe')

    # nested
    # display('John Doe')

    # DRY - Don't Repeat Yourself
    display_info("John", 25)
    error_func()
    find_even_numbers()

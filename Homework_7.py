# task1:
import random


def retry(attempts=5, desired_value=None):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            for _ in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print("Failure.")
        return func_wrapper
    return decorator


@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


get_random_value_with_default_attempts()
get_random_values_with_default_attempts([1, 2, 3, 4])
get_random_values_with_default_attempts([1, 2, 3, 4], 2)
get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
get_random_values([1, 2, 3, 4])
get_random_values([1, 2, 3, 4], 3)
get_random_values([1, 2, 3, 4], size=1)


# task 2:
def copy_file(source_path, destination_path):
    source_file = open(source_path, 'r')
    content = source_file.read()
    destination_file = open(destination_path, 'w')
    destination_file.write(content)
    source_file.close()
    destination_file.close()


copy_file('Source_file.txt', 'Destination_file.txt')

# task 3:

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


# get_random_value()
# get_random_value_with_default_attempts()
# get_random_values_with_default_attempts([1, 2, 3, 4])
# get_random_values_with_default_attempts([1, 2, 3, 4], 2)
# get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
# get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
# get_random_values([1, 2, 3, 4])
# get_random_values([1, 2, 3, 4], 3)
# get_random_values([1, 2, 3, 4], size=1)
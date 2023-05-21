def get_unique_elements(*args):
    unique_elements = []
    for arg in args:
        if arg not in unique_elements:
            unique_elements.append(arg)
    return unique_elements


def print_argument_count(**kwargs):
    argument_count = len(kwargs)
    user_type = kwargs.get("user_type", "Student")
    print("Number of arguments:", argument_count)
    print("Value of 'user_type':", user_type)


def positional_and_keyword(arg1, arg2, arg3=None, arg4=None, arg5=None):
    pass


def multiply_function(arg):
    def inner_multiply(inner_arg):
        return arg * inner_arg

    return inner_multiply


def print_square(length, end_flag=None):
    print("*" * length)
    if end_flag is None:
        print_square(length, end_flag)

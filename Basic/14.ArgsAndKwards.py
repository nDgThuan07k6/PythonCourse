def describe_person(*args, **kwargs):
    # * use for single value
    print('Hobby: ')
    for hobby in args:
        print('-', hobby)

    # ** use for double value (1. For key, 2. For value)
    print('User profile: ')
    # ** use .items()
    for key, value in kwargs.items():
        print(f'{key.capitalize()}: {value}')

describe_person('Reading', 'Play game', 'Travel', name = 'Thuan', age = 20, city = 'Ho Chi Minh')
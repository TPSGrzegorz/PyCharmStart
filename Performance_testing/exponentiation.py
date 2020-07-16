import timeit


def new_power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    half_exponent = exponent // 2
    half_result = new_power(base, half_exponent)

    result = half_result * half_result
    if exponent % 2 == 0:
        return result
    else:
        return result * base


def standard_power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    else:
        return base * standard_power(base, exponent - 1)


def new_power_time():
    SETUP_CODE = ''' 
from __main__ import new_power'''

    TEST_CODE = '''  
new_power(2, 2048)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100000)

    # priniting minimum exec. time
    print(f'New_power time: {min(times)}')


def standard_power_time():
    SETUP_CODE = ''' 
from __main__ import standard_power'''

    TEST_CODE = '''  
standard_power(2, 512)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100000)

    # priniting minimum exec. time
    print(f'Standard_power time: {min(times)}')


new_power_time()
standard_power_time()

import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG)


def add(x, y):
    """Adding funtion"""
    return x + y

def subtract(x, y):
    """Subtract Funtion"""
    return x - y

def mutiply(x, y):
    """Multiply funtion"""
    return x * y

def divide(x, y):
    """Divide funtion"""
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)

logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)

logging.debug('Subtract: {} + {} = {}'.format(num_1, num_2, sub_result))
# logging.warning('Subtract: {} + {} = {}'.format(num_1, num_2, sub_result))

mul_result = mutiply(num_1, num_2)

logging.debug('Mul: {} + {} = {}'.format(num_1, num_2, mul_result))
# logging.warning('Mul: {} + {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)

# logging.warning('div: {} + {} = {}'.format(num_1, num_2, div_result))
logging.debug('div: {} + {} = {}'.format(num_1, num_2, div_result))

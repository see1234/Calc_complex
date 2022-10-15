def view_data(data, title):
    print(f'{title} = {data}')


def view_data_lst(data, title):
    znak = '+' if data[1] > 0 else '-'
    print(f'{title} = {data[0]}{znak}{abs(data[1])}*i')
    return f'{data[0]}{znak}{abs(data[1])}*i'


def get_value():
    return input('value = ')


def get_op():
    return input('operation (+, -, *, /) = ')

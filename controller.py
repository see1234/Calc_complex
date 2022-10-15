import complex_calc as cc
import real_calc as rc

import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_op = view.get_op()

    if 'i' in value_a or 'i' in value_b:
        value_a_lst = list(map(int, value_a.replace('i', '').split()))
        value_b_lst = list(map(int, value_b.replace('i', '').split()))
        print(value_a_lst)
        print(value_b_lst)
        cc.init(value_a_lst, value_b_lst)
        result = cc.do_it(value_op)
        view.view_data_lst(result, "result")
    else:
        value_a = int(value_a)
        value_b = int(value_b)
        rc.init(value_a, value_b)
        result = rc.do_it(value_op)
        view.view_data(result, "result")


if __name__ == '__main__':
    button_click()

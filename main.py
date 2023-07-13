from calculator.controller import parantes_stack_resolver, stack_optimizer
from calculator.calculation import calculate


def calculator(s):
    # white space make works hard also thay are unnecessary so we delete them
    s = s.replace(' ', '')
    s = s.replace('\u03C0', 'pi')
    li = parantes_stack_resolver(s)
    li = stack_optimizer(li)
    result = calculate(li)

    # because of using numberical calculation
    # it is possible numbers be Approximate but using just 5 digit is ok

    def check_float(fl):
        fl = round(fl, 5)
        if fl.is_integer():
            fl = int(fl)
        return fl

    if isinstance(result, complex):
        result = (check_float(result.real), check_float(result.imag))

    elif isinstance(result, float):
        result = (check_float(result), 0)

    return result

from utils import turn_to_number, operators
from math import cos, sin, tan, log10, log


def cot(v):
    return 1/tan(v)


functions = {
    'cos': cos,
    'sin': sin,
    'tan': tan,
    'cot': cot,
    'log': log10,
    'ln': log,
}


class Function():
    handler = None
    args = []

    def __init__(self, handler, args):
        self.handler = handler
        self.args = args
        self.args_parser()

    # find function arguments and seperate them with ',' and pass them to function
    # EXAMPLE: [ '1' , '+' , '3' , ',' , '4' ] -> [['1','+','3'],['4']]
    def args_parser(self):
        buffer = []
        result = []

        for i in self.args:
            if i == ',':
                result.append(buffer)
                buffer = []
            else:
                buffer.append(i)

        result.append(buffer)
        self.args = result

    def operate(self):
        args = []
        for arg in self.args:
            args.append(calculate(arg))

        return self.handler(*args)

    def __str__(self):
        return f" { str(self.handler) }({self.args}) "

    def __repr__(self):
        return f" { repr(self.handler) }({self.args}) "


def calculate(stack):
    """
        this function calculate a tokenized stack
        using recursion method ( walk through tree )
    """
    if len(stack) == 1:
        obj = stack[0]

        if isinstance(obj, list):
            return calculate(obj)

        elif isinstance(obj, Function):
            return obj.operate()

        elif isinstance(obj, str):
            number = turn_to_number(obj)
            if number is None:
                raise Exception("object is not a valid number")
            return number

    for operator in operators.keys():
        for token_idx in range(len(stack)):
            if stack[token_idx] == operator:
                left = stack[:token_idx]
                right = stack[token_idx+1:]
                left_number = calculate(left)
                right_number = calculate(right)
                a = operators[operator](left_number, right_number)
                return a

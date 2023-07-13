from .utils import operators, get_index
from .calculation import functions, Function
from math import pi


def multiple_normalze(li):
    #   add '*' token if there is no operation
    #   between a list and it's before object
    #   example: 2(2+5) -> 2*(2+5)
    if not li:
        return li

    result = [li[0], ]
    for i in range(1, len(li)):
        if isinstance(li[i], list) and li[i-1] not in operators.keys():
            result.append('*')
        result.append(li[i])
    return result


def function_normalize(li):
    #   check is a item in function list and if yes,
    #   create a Function obj then add it to stack
    #   example:
    #   [ '2' , '+' , 'cos', ['pi','/', '2'] ] -> [[ '2' , '+' , Function(cos) ]]

    result = []
    i = 0
    while i < len(li):
        item = get_index(li, i+1, None)
        if isinstance(item, list) and li[i] in functions.keys():
            result.append(Function(functions[li[i]], item))
            i += 1
        else:
            result.append(li[i])
        i += 1

    return result


def pi_normalize(li):
    #   turn all 'pi' tokens to it's number
    result = []
    for i in li:
        if i == 'pi':
            result.append(str(pi))
        else:
            result.append(i)

    return result


def normalize(li):
    li = pi_normalize(li)
    li = function_normalize(li)
    li = multiple_normalze(li)
    return li


def tokenize(li):
    #   this function tokenize given list by operators
    #   example:
    #   [ '2+3.4*cos', ['pi/2'] ] -> [ '2','+','3.4','*','cos', ['pi','/','2'] ]

    buffer = ''
    result = []

    def flush_buffer(result, buffer):
        if buffer:
            result.append(buffer)
            buffer = ''
        return (result, buffer)

    for item in li:
        if not isinstance(item, str):
            result, buffer = flush_buffer(result, buffer)
            result.append(item)
        else:
            for i in item:
                if i in operators.keys():
                    result, buffer = flush_buffer(result, buffer)
                    result.append(i)
                else:
                    buffer += i
            result, buffer = flush_buffer(result, buffer)

    return result


# NOTE: this function use walker algorithm with recursion method
def stack_optimizer(li):
    for i in range(len(li)):
        if isinstance(li[i], list):
            li[i] = stack_optimizer(li[i])

    # now we are in the deepest stack
    return normalize(tokenize(li))


def parantes_stack_resolver(s):
    #  this function segmentate given string to
    #  nested arraies (by paranteses) to make solving sentence easier
    #  it's use stack and heap algorithm
    #  Graph of a example :
    #         1 + 2 * ( 4i + (1 / 5 ) + ( 2 ^ 2 * 5i) ) + 1
    #  row1:  -------\                                 /-----
    #  row2:          \------\       /--\             /
    #  row3:                  \-----/    \-----------/
    #  sentences will solve by stack_calculator function from bottom to top

    base_stack = []
    buf = ""
    heap = [
        base_stack,
    ]

    for i in range(len(s)):
        if s[i] == '(':
            if buf:  # if buf exists add this to last stack
                last_stack = heap[len(heap)-1]
                last_stack.append(buf)
                buf = ''
            # add new stack to heap
            heap.append([])

        elif s[i] == ')':
            # if heap have more than one stack (base stack)
            # add ended stack to its parent stack then clear ended stack
            if len(heap) > 1:
                last_stack = heap[len(heap)-1]

                if buf:
                    last_stack.append(buf)
                    buf = ''

                befor_stack = heap[len(heap)-2]
                befor_stack.append(last_stack)

            heap.pop()

        else:
            buf += s[i]

    if buf:
        base_stack.append(buf)

    return base_stack

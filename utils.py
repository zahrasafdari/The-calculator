from operator import pow, truediv, mul, add, sub
import re


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '\u00f7': truediv,
    '^': pow,
}


def turn_to_number(element):
    #   this function use regex to detect if given string
    #   is number (and if it is imaginary or real) or not
    imag = re.match(r'^-?\d+(?:\.\d+)?(j|i)?$', element)
    real = re.match(r'^-?\d+(?:\.\d+)?$', element)
    if real:
        return float(element)
    if imag:
        # python determain complex numbers with j
        # so we must change all i to j
        element = element.replace('i', 'j')
        return complex(element)
    return None


def get_index(li, idx, default):
    try:
        return li[idx]
    except IndexError:
        return default

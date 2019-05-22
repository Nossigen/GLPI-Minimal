import sys

from .models import string_helper


def check_header(string_send):
    hstr = string_helper()
    line = ''

    hstr.parse(string_send)
    line = hstr.get(12)

    if (line == ''):
        print('[Error] - Wrong header', sys.stderror)
        return false
    return true
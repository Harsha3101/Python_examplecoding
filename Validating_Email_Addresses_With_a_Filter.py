import re

regex = re.compile(r'[A-Za-z0-9_-]+[@][A-Za-z0-9]+\.[A-Z|a-z]{2,3}')

def fun(s):
    # return True if s is a valid email, else return False
    return bool(re.fullmatch(regex, s))

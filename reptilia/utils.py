import string
import random
import inspect
from bs4 import BeautifulSoup


def generate_unique_string(length = 10):
    charset = string.ascii_uppercase + string.ascii_lowercase + '_'
    return ''.join([random.choice(charset) for _ in range(length)])


def get_class_fields(cls, excluded=[]):
    l = []
    for i in inspect.getmembers(cls):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                l.append(i)
    result = []
    for i in l:
        if not i[0] in excluded:
            result.append(i[0])
    return result


def prettify(code):
    soup = BeautifulSoup(code, "html.parser")
    return soup.prettify().strip()

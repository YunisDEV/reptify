from .base import Element


class Div(Element):
    tagName = 'div'


class P(Element):
    tagName = 'p'


class Img(Element):
    tagName = 'img'


class A(Element):
    tagName = 'a'


class ElementSet:
    div = Div
    p = P
    img = Img

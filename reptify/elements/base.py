from jinja2 import Template
from ..utils import prettify,generate_unique_string

class Base:
    className = None
    style = None
    body = None
    tagName = None
    attrs = {}
    template_string = """
        <{{tagName}} 
            {%if id%}id="{{id}}"{%endif%}
            {%if className%}class="{{className}}"{%endif%}
            {%if style%}style="{{style.getCss()}}"{%endif%}
            {%for key,value in attrs.items()%}
            {{key}}={{value}}
            {%endfor%}
        >
            {{innerHTML}}
        </{{tagName}}>
    """
    secure_fields = ['attrs', 'body', 'className', 'id', 'style', 'tagName', 'template_string']

    def __init__(self, tag='div'):
        self.tagName = tag

    def render(self, *args, **kwargs):
        temp = Template(self.template_string)
        innerHTML = ''
        for part in self.body:
            if not isinstance(part, str):
                innerHTML += part.render()
            else:
                innerHTML += part
        rendered_html = temp.render(id=self.id, className=self.className,
                                    style=self.style, innerHTML=innerHTML, tagName=self.tagName, attrs=self.attrs)
        return prettify(rendered_html)

    def applyStyles(self, style_object):
        self.style = style_object


class Element(Base):
    def __init__(self, body="", className=None, style=None, ** attrs):
        self.id = generate_unique_string()
        self.body = [body] if not isinstance(
            body, list) or isinstance(body, tuple) else body
        self.className = className
        self.style = style
        self.attrs = attrs

    def getAttr(self,key):
        if not key in self.secure_fields:
            return self.attrs.get(key,None)
        else:
            raise Exception('Can not change this attribute')
    
    def setAttr(self,key,value):
        if not key in self.secure_fields:
            self.attrs[key] = value
        else:
            raise Exception('Can not change this attribute')
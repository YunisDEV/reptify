from jinja2 import Template
from ..utils import get_class_fields

class ScriptBase():
    template = """"""

    def getHTML(self):
        template = Template(self.template)
        return template.render(**self.__dict__)

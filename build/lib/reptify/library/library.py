from jinja2 import Template
from ..utils import prettify


class Library:
    def __init__(self, href, fileType=None, **attrs):
        if not fileType:
            self.fileType = href.split('.')[-1].lower()
        else:
            self.fileType = fileType
        self.href = href
        self.attrs = attrs

    def getHTML(self):
        temp = Template("")
        if self.fileType == 'js':
            temp = Template("""
            <script src="{{href}}"
            {%for key,value in attrs.items()%}
            {{key}}="{{value}}"
            {%endfor%}
            ></script>
            """)
        elif self.fileType == 'css':
            temp = Template("""
            <link rel="stylesheet" href="{{href}}"
            {%for key,value in attrs.items()%}
            {{key}}="{{value}}"
            {%endfor%}
            >
            """)
        return prettify(temp.render(href=self.href, attrs=self.attrs))


def Libraries(*args):
    return [Library(i) for i in args]

def generate_library_list_html(libs):
    return "\n".join([i.getHTML() for i in libs])
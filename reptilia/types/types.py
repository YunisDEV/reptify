from ..utils import prettify
from ..library.library import generate_library_list_html
from ..script.scripts import generate_script_list_html


class HTMLFile:
    def __init__(self, body):
        if not isinstance(body, str):
            body = body.render()
        self.body = prettify(body)

    def export(self, filename):
        f = open(filename, 'wt')
        f.write(self.body)


class HTMLBase:
    title = "Unnamed"
    libs = []
    scripts = []
    content = ""
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {libs}
    </head>
    <body>
        {content}
        <script>
            {scripts}
        </script>
    </body>
    </html>
    """

    def __init__(self, content=None, template=None, libs=None, scripts=None, title=None):
        if template:
            self.template = template
        if content:
            self.content = content
        if libs:
            self.libs = libs
        if scripts:
            self.scripts = scripts
        if title:
            self.title = title

    def insertLibrary(self, lib):
        self.libs.append(lib)

    def insertScript(self, script):
        self.scripts.append(script)

    def render(self):
        if isinstance(self.content, str):
            content = self.content
        else:
            content = self.content.render()
        return prettify(self.template.format(
            content=content,
            title=self.title,
            libs=generate_library_list_html(self.libs),
            scripts=generate_script_list_html(self.scripts)
        ))

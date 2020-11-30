from .base import ScriptBase


class ScriptEventListener(ScriptBase):
    template = """
        document.getElementById('{{id}}').addEventListener('{{event}}',function(e){
            {{callback}}
        })
    """

    def __init__(self, element, event="click", callback=""):
        self.element = element
        self.id = self.element.id
        self.event = event
        if not isinstance(callback, str):
            cb = callback.getHTML()
        else:
            cb = callback
        self.callback = cb


class ScriptAlert(ScriptBase):
    template = """
        window.alert('{{text}}'{%if title%},'{{title}}'{%endif%})
    """

    def __init__(self, text="",title=None):
        self.text = text
        self.title = title

class Scripts:
    EventListener = ScriptEventListener
    Alert = ScriptAlert


def generate_script_list_html(scripts):
    return "\n".join([script.getHTML() for script in scripts])

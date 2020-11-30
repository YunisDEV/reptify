from reptilia import (
    ElementSet as dom,
    HTMLBase,
    Scripts as js,
    Libraries,
    HTMLFile
)

hello_p = dom.p('Hello')

container = dom.div(
    body=[
        hello_p,
        dom.p('How are you?')
    ],
    className="container"
)

home_page = HTMLBase(container)

home_page.insertScript(
    js.EventListener(hello_p,'click',
        js.Alert('HELLO!!!')
    )
)

HTMLFile(home_page).export('blabla.html')
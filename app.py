from fasthtml.common import *

app,rt = fast_app(pico=False,
                  hdrs=(
                      Link(rel='stylesheet', href='style.css', type='text/css'),
                  ))

@rt('/')
def get(): return Div(P(''), cls="circle", hx_get="/change")


@rt('/change')
def get(): return P('Please do not press this button again')

serve()
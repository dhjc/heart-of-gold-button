from fasthtml.common import *

app,rt = fast_app(pico=False,
                  hdrs=(
                      Link(rel='stylesheet', href='style.css', type='text/css'),
                  ))

@rt('/')
def get(): return Div(Div(P(''), cls="circle", hx_get="/change"), Div(P('Starship "Heart of Gold"'), hx_swap_oob=True, id="credit", cls='footer'))


@rt('/change')
def get(): return P('Please do not press this button again'), Div('Hitchhikers Guide to the Galaxy, by Douglas Adams.', hx_swap_oob='innerHTML:#credit')


serve()
import os
import jinja2

env = jinja2.Environment()
template = env.from_string("hello, {{ name }}")
template.render(name='world')
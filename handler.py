"""
Defines main handler superclass.
"""
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)
    
    def render_str(self, template, **kwargs):
        t = jinja_env.get_template(template)
        return t.render(kwargs)
    
    def render(self, template, **kwargs):
        kwargs['page'] = template.replace(".html", "")
        print kwargs['page']
        self.write(self.render_str(template, **kwargs))
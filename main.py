"""
Contains route handlers.
"""
import webapp2

from handler import Handler

class FrontPageHandler(Handler):
    """
    Serves the first page
    """
    def get(self):
        self.render("index.html")

class ProjectsPageHandler(Handler):
    """
    Serves the projects page
    """
    def get(self):
        self.render("projects.html")

class ResumePageHandler(Handler):
    """
    Serves the resume page
    """
    def get(self):
        self.render("resume.html")

ROUTES = [
    ('/', FrontPageHandler),
    ('/projects', ProjectsPageHandler),
    ('/resume', ResumePageHandler)
]

app = webapp2.WSGIApplication(ROUTES, debug=False)

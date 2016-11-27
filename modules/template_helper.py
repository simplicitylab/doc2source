"""
    Module for the Template helper class

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
# standard library
import os

# jinja2
from jinja2 import Template

class TemplateHelper(object):
    """ Template class  """

    def get_template_path(self, template_name):
        """ Get template path """
        return os.path.join(os.path.dirname(__file__), "../templates/%s" % template_name)

    def load_template(self, template_name):
        """ Load template """
        return open(self.get_template_path(template_name), "r").read()

    def render(self, template_name, template_vars_dict):
        """ Render template """
        template = Template(self.load_template(template_name))
        return template.render(template_vars_dict)

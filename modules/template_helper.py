"""
    Module for the Template helper class

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
# standard library
import os

# jinja2
from jinja2 import Environment, FileSystemLoader
from jinja2_pluralize import pluralize

class TemplateHelper(object):
    """ Template class  """
    def __init__(self):
        """ Default constructor """
        template_dir = os.path.join(os.path.dirname(__file__), "../templates/")
        self.j2_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
        self.j2_env.filters['pluralize'] = pluralize

    def render(self, template_name, template_vars_dict):
        """ Render template """
        return self.j2_env.get_template(template_name).render(template_vars_dict)


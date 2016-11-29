"""
    Module for the doctrine generator

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
import os
from ..template_helper import TemplateHelper

class DoctrineGenerator(object):
    """Doctrine generator"""

    def __init__(self):
        """ Constructor """
        self.template_helper = TemplateHelper()

    def get_supported_parsers(self):
        """ Get list of supported parsers """
        return ['dbdoc']

    def get_name(self):
        """ Get name of generator """
        return "doctrine"

    def generate(self, parse_result, output_filename):
        """ Generate document """
        # render template
        source = self.template_helper.render("doctrine.tpl", {})

        # write to file
        output_file = open(output_filename, "w")
        output_file.write(source)
        output_file.close()

"""
    Module for the titanic json generator

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
import json
from ..template_helper import TemplateHelper

class TitanicGenerator(object):
    """Doctrine generator"""

    def __init__(self):
        """ Constructor """
        self.template_helper = TemplateHelper()

    def get_supported_parsers(self):
        """ Get list of supported parsers """
        return ['titanic']

    def get_name(self):
        """ Get name of generator """
        return "titanic"

    def generate(self, parse_result, output_filename):
        """ Generate document """

        entry_list = []
        for entry in parse_result:
            entry_dict = {}
            entry_dict["name"] = " ".join(entry.name)
            entry_dict["sex"] = entry.sex
            entry_dict["age"] = entry.age
            entry_dict["class"] = entry.ship_class
            entry_dict["survived"] = "yes" if int(entry.survived) else "no"
            entry_list.append(entry_dict)

        # write to file
        output_file = open(output_filename, "w")
        output_file.write(json.dumps(entry_list))
        output_file.close()

"""
    Module for the doctrine generator

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
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

        # loop over entities
        for entity in parse_result:
            template_vars_dict = {}
            # create variables
            template_vars_dict["table_name"] = entity.Name.lower().replace(" ", "_")

            # Car bike -> CarBike
            name_splitted = [s.title() for s in entity.Name.split(" ")]
            template_vars_dict["entity_name"] = "".join(name_splitted)

            # create Fields list containing dictionaries
            fields = []
            for field in entity.Fields:
                # My variable -> myVariable
                name_splitted = [s.title() for s in field.Name.split(" ")]
                variable_name = "".join(name_splitted)
                variable_name = variable_name[0].lower() + variable_name[1:]

                method_name = "".join(name_splitted)

                fields.append({
                    "name" : field.Name,
                    "variable_name" : variable_name,
                    "type" : field.Type,
                    "method_name" : method_name
                    })
            template_vars_dict["fields"] = fields

            # render template
            source = self.template_helper.render("doctrine.tpl", template_vars_dict)

            # write to file
            output_file = open("%s.php" % template_vars_dict["entity_name"], "w")
            output_file.write(source)
            output_file.close()

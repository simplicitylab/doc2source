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

    def get_table_name(self, name):
        """ Get table name  """
        return name.lower().replace(" ", "_")

    def get_variable_name(self, name):
        """
        Get variable name

        My variable -> myVariable
        """
        name_splitted = [s.title() for s in name.split(" ")]
        variable_name = "".join(name_splitted)
        variable_name = variable_name[0].lower() + variable_name[1:]
        return variable_name

    def get_entity_name(self, name):
        """
        Get entity name

        Car bike -> CarBike
        """
        name_splitted = [s.title() for s in name.split(" ")]
        return "".join(name_splitted)

    def generate(self, parse_result, output_filename):
        """ Generate document """

        # hold relationships
        known_relationships = []

        # loop over entities
        for entity in parse_result:
            template_vars_dict = {}
            # create variables
            template_vars_dict["table_name"] = self.get_table_name(entity.Name)
            template_vars_dict["entity_name"] = self.get_entity_name(entity.Name)

            # create Fields list containing dictionaries
            fields = []
            for field in entity.Fields:
                variable_name = self.get_variable_name(field.Name)

                method_name = "".join([s.title() for s in field.Name.split(" ")])

                extras = []
                for extra in field.Extras:
                    extras.append(extra)

                relationship = {}
                if field.Relationship:
                    # process relationship
                    relationship_type = ""

                    if field.Relationship.Direction == "->":
                        relationship_type = "ManyToOne"

                    # store relationship
                    relationship["type"] = relationship_type
                    relationship["sourceName"] = self.get_variable_name(entity.Name)
                    relationship["mappedBy"] = self.get_entity_name(entity.Name)
                    relationship["targetEntity"] = self.get_entity_name(field.Relationship.Target)
                    known_relationships.append(relationship)
                else:
                    # check if a reverse relationship exists
                    for known_relationship in known_relationships:
                        if known_relationship['targetEntity'] == entity.Name:
                            pass

                fields.append({
                    "name" : field.Name,
                    "variable_name" : variable_name,
                    "type" : field.Type,
                    "method_name" : method_name,
                    "extras" : extras,
                    "relationship": relationship
                    })
            template_vars_dict["fields"] = fields

            # render template
            source = self.template_helper.render("doctrine.tpl", template_vars_dict)

            # write to file
            output_file = open("%s.php" % template_vars_dict["entity_name"], "w")
            output_file.write(source)
            output_file.close()

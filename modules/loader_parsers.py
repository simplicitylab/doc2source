""" Module load parsers """
import glob
import os

class LoaderParsers(object):
    """ Parsers loader class """

    def __init__(self):
        """ Default constructor """
        self.available_parsers = {}
        self.get_local_parsers()

    def validate_parser(self, parser_class):
        """ validates parsers """
        class_properties_methods = parser_class.__dict__

        # check if class has certain methods
        if not "define_document_grammar" in class_properties_methods:
            return False

        if not "parse_file" in class_properties_methods:
            return False

        return True

    def load_parser(self, py_filename):
        """ Load parser """
        # create names
        parser_name = os.path.splitext(py_filename)[0]
        parser_class_name = "%sParser" % parser_name.title()
        module_name = "modules.parsers.%s" % parser_name

        # load class dynamically
        mod = __import__(module_name, fromlist=[parser_class_name])
        parser_class = getattr(mod, parser_class_name)

        # check if parser is valid class
        is_valid_parser_class = self.validate_parser(parser_class)

        if is_valid_parser_class:
            # store class object in dictionary available_parsers
            self.available_parsers[parser_name] = parser_class()
        else:
            raise Exception("Parser %s is invalid parser" % parser_name)

    def get_local_parsers(self):
        """ Get parsers """
        for py_file_path in glob.glob("modules/parsers/*.py"):
            # get basename
            python_file = os.path.basename(py_file_path)

            # skip init python file
            if python_file != "__init__.py":
                self.load_parser(python_file)

    def get_parsers(self):
        """ Get available parsers """
        return self.available_parsers

    def get_parsers_names(self):
        """ Get parser names """
        return self.available_parsers.keys()

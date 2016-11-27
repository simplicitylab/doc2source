"""
    Module that handles the loading of generators

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
import glob
import os

class LoaderGenerators(object):
    """ Generators loader class """
    def __init__(self):
        """ Default constructor """
        self.available_generators = {}
        self.get_local_generators()

    def validate_generator(self, generator_class):
        """ validates generator """
        class_properties_methods = generator_class.__dict__

        # check if class has certain methods
        if not "get_name" in class_properties_methods:
            return False

        if not "get_supported_parsers" in class_properties_methods:
            return False

        if not "generate" in class_properties_methods:
            return False

        return True

    def load_generator(self, py_filename):
        """ Load generator """
        # create names
        generator_name = os.path.splitext(py_filename)[0]
        generator_class_name = "%sGenerator" % generator_name.title()
        module_name = "modules.generators.%s" % generator_name

        # load class dynamically
        mod = __import__(module_name, fromlist=[generator_class_name])
        generator_class = getattr(mod, generator_class_name)

        # check if generator is valid class
        is_valid_generator_class = self.validate_generator(generator_class)

        if is_valid_generator_class:
            # store class object in dictionary available_generators
            self.available_generators[generator_name] = generator_class()
        else:
            raise Exception("Generator %s is invalid generator" % generator_name)

    def get_local_generators(self):
        """ Get available generators """
        for py_file_path in glob.glob("modules/generators/*.py"):
            # get basename
            python_file = os.path.basename(py_file_path)

            # skip init python file
            if python_file != "__init__.py":
                self.load_generator(python_file)

    def get_generators(self):
        """ Get generators """
        return self.available_generators

    def get_generators_names(self):
        """ Get generators names """
        return self.available_generators.keys()

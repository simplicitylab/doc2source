"""
    Module for the doctrine generator

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
class DoctrineGenerator(object):
    """Doctrine generator"""

    def __init__(self):
        """ Constructor """
        pass

    def is_parser_supported(self, parser_name):
        """ Checks if parser is supported """
        if parser_name in self.get_supported_parsers():
            return True
        else:
            return False

    def get_supported_parsers(self):
        """ Get list of supported parsers """
        return ['dbdoc']

    def get_name(self):
        """ Get name of generator """
        return "doctrine"

    def generate(self, output_filename):
        """ Generate """
        print "generate file %s" % output_filename

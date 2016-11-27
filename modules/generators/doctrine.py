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

    def get_supported_parsers(self):
        """ Get list of supported parsers """
        return ['dbdoc']

    def get_name(self):
        """ Get name of generator """
        return "doctrine"

    def generate(self, parse_result, output_filename):
        """ Generate document """
        print "generate file %s" % output_filename

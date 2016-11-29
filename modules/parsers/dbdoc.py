"""
    Module for the 'DBDoc' document parser (using pyparsing)

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
from pyparsing import Word, Literal, Suppress, Group, OneOrMore, Optional, alphanums

class DbdocParser(object):
    """ DbdocParser class """

    def __init__(self):
        """ Constructor """
        self.define_document_grammar()

    def define_document_grammar(self):
        """ Define document grammar rules """
        # define symbol expressions
        double_hash = Suppress(Literal("##"))
        star = Suppress(Literal("*"))
        comma_l = Suppress(Literal("("))
        comma_r = Suppress(Literal(")"))
        text = OneOrMore(Word(alphanums)).setParseAction(lambda tokens: " ".join(tokens))

        # define structural expressions
        entity_name = double_hash + text.setResultsName("EntityName")
        entity_field_attributes = comma_l + text.setResultsName("Attributes") + comma_r
        entity_field_name = star + text.setResultsName('Name')
        entity_field = Group(entity_field_name + Optional(entity_field_attributes)) \
        .setResultsName('Field')
        entity_fields = Group(OneOrMore(entity_field)).setResultsName('Fields')
        entity_structure = entity_name + entity_fields

        # store final expression
        self.final_expression = entity_structure

    def parse(self, string_to_parse):
        """ Parse file """
        return self.final_expression.searchString(string_to_parse)

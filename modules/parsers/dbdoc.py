"""
    Module for the 'DBDoc' document parser (using pyparsing)

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
from pyparsing import Word, Literal, Suppress, Group, OneOrMore, Optional, alphanums, Combine

class DbdocParser(object):
    """ DbdocParser class """

    def __init__(self):
        """ Constructor """
        self.define_document_grammar()

    def define_document_grammar(self):
        """ Define document grammar rules """
        # define symbol expressions
        double_hash = Literal('##')
        star = Literal('*')
        parenthesis_l = Literal('(')
        parenthesis_r = Literal(')')
        comma = Literal(',')
        equal = Literal('=')
        quote = Literal('"')
        arrow_right = Literal('->')

        # define text structures
        text = OneOrMore(Word(alphanums)).setParseAction(lambda tokens: " ".join(tokens))
        parameter = Combine(text + equal + Optional(quote) + text + Optional(quote))

        # define structural expressions
        entity_name = double_hash + text.setResultsName("Name")

        entity_field_attributes = Suppress(parenthesis_l) + text.setResultsName('Type') + \
        Optional(OneOrMore(Suppress(comma) + (parameter|text).setResultsName('Extra'))) \
        .setResultsName('Extras') + Suppress(parenthesis_r)

        entity_field_relationship = Group(arrow_right.setResultsName('Direction') + \
        text.setResultsName('Target')).setResultsName('Relationship')

        entity_field_name = star + text.setResultsName('Name')

        entity_field = Group(entity_field_name + Optional(entity_field_attributes| \
        entity_field_relationship)).setResultsName('Field')

        entity_fields = Group(OneOrMore(entity_field)).setResultsName('Fields')
        entity_structure = entity_name + entity_fields

        # store final expression
        self.final_expression = entity_structure

    def parse(self, string_to_parse):
        """ Parse file """
        return self.final_expression.searchString(string_to_parse)

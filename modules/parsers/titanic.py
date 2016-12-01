"""
    Module for the 'titanic'  parser (using pyparsing)

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
from pyparsing import alphas, alphanums, nums, Word, Literal, Suppress, OneOrMore

class TitanicParser(object):
    """ DbdocParser class """

    def __init__(self):
        """ Constructor """
        self.define_document_grammar()

    def define_document_grammar(self):
        """ Define document grammar rules """

        """
        Backus Naur Form (BNF)

        chars    ::= a-zA-Z
        numbers  ::= 0-1
        word     ::= chars|numbers+
        number   ::= numbers+
        quote    ::= '"'
        comma    ::= ','

        name     ::= quote word+ quote
        class    ::= number+
        age      ::= number+
        sex      ::= word
        survived ::= number
        entry    ::= name class agen sex survived
        """
        quote = Literal('"')
        comma = Literal(',')

        name = Suppress(quote) + OneOrMore(Word(alphas)|Suppress(comma)) + Suppress(quote)
        ship_class = Word(alphanums)
        age = Word(nums)
        sex = Word(alphanums)
        survived = Word(nums)

        entry = name.setResultsName('name') + ship_class.setResultsName('ship_class') \
        + age.setResultsName('age') + sex.setResultsName('sex') \
        + survived.setResultsName('survived')

         # store final expression
        self.final_expression = entry

    def parse(self, string_to_parse):
        """ Parse file """
        return self.final_expression.searchString(string_to_parse)

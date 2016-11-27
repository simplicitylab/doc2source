"""
    Doc2Source

    Blueprint framework that lets you generate sourcecode from documents

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
# standard library
import argparse
import sys

# doc2source modules
from modules.loader_generators import LoaderGenerators
from modules.loader_parsers import LoaderParsers

def load_parsers_generators():
    """ Load parsers and generators """
    loader_generators = LoaderGenerators()
    loader_parsers = LoaderParsers()

    return loader_parsers, loader_generators

def process_parameters():
    """ Process parameters """
    # setup argument parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('--list-parsers', action='store_true', help='lists parsers')
    parser.add_argument('--list-generators', action='store_true', help='lists generators')
    parser.add_argument('parser_name', nargs='?', help='name of parser')
    parser.add_argument('generator_name', nargs='?', help='name of generator')
    parser.add_argument('output_name', nargs='?', help='name of output file')

    # parse arguments
    args = parser.parse_args()

    return args

def main():
    """ Main entry """

    # load parsers and generators
    loader_parsers, loader_generators = load_parsers_generators()

    # process commandline arguments
    args = process_parameters()

    # if we need to list things
    if args.list_parsers:
        for parser in loader_parsers.get_parsers_names():
            print "* %s" % parser

    if args.list_generators:
        for generator in loader_generators.get_generators_names():
            print "* %s" % generator


if __name__ == "__main__":
    main()

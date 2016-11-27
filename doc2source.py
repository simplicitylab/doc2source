"""
    Doc2Source

    Blueprint framework that lets you generate sourcecode from documents

    written by Glenn De Backer < glenn at simplicity dot be>
    License: GPLv2
"""
# standard library
import argparse

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
    parser.add_argument('--list-parsers', action='store_true', help='lists available parsers')
    parser.add_argument('--list-generators', action='store_true', help='lists available generators')
    parser.add_argument('parser_name', nargs='?', help='name of parser')
    parser.add_argument('generator_name', nargs='?', help='name of generator')
    parser.add_argument('output_filename', nargs='?', help='name of output file')

    # parse arguments
    args = parser.parse_args()

    return args, parser

def read_file(filename):
    """ Read file """
    return open(filename, 'r').read()

def main():
    """ Main entry """

    # load parsers and generators
    loader_parsers, loader_generators = load_parsers_generators()

    # process commandline arguments
    args, argument_parser = process_parameters()

    # if we need to list things
    if args.list_parsers:
        for parser in loader_parsers.get_parsers_names():
            print "* %s" % parser

    if args.list_generators:
        for generator in loader_generators.get_generators_names():
            print "* %s" % generator

    # be sure that everythig is passed to generate "source"
    if args.parser_name is None \
    or args.generator_name is None \
    or args.output_filename is None:
        argument_parser.print_help()
    else:
        pass

if __name__ == "__main__":
    main()

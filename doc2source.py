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

def get_parser_generator(parser_name, generator_name, loaded_parsers, loaded_generators):
    """ get parser and generator choice """

    # check if parser and generator is valid choice
    if parser_name not in loaded_parsers.get_parsers_names():
        raise Exception("Parser was not found")

    if generator_name not in loaded_generators.get_generators_names():
        raise Exception("Generator was not found")

    # get requested parser and generator
    parser = loaded_parsers.get_parsers()[parser_name]
    generator = loaded_generators.get_generators()[generator_name]

    # check if parser is supported by our generator
    if parser_name not in generator.get_supported_parsers():
        raise Exception("Parser not supported by generator")

    return parser, generator

def process_parameters():
    """ Process parameters """
    # setup argument parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('--list-parsers', action='store_true', help='lists available parsers')
    parser.add_argument('--list-generators', action='store_true', help='lists available generators')
    parser.add_argument('parser_name', nargs='?', help='name of parser')
    parser.add_argument('generator_name', nargs='?', help='name of generator')
    parser.add_argument('input_filename', nargs='?', help='name of file that needs to be parsed')
    parser.add_argument('output_filename', nargs='?', help='name of output file (if supported by generator)')

    # parse arguments
    args = parser.parse_args()

    return args, parser

def read_file(filename):
    """ Read file """
    return open(filename, "r").read()

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

    elif args.list_generators:
        for generator in loader_generators.get_generators_names():
            print "* %s" % generator

    elif args.parser_name is None \
    or args.generator_name is None \
    or args.input_filename is None:
        argument_parser.print_help()
    else:
        # get parser and generator, which also validates choices
        parser, generator = get_parser_generator(args.parser_name, args.generator_name, \
        loader_parsers, loader_generators)

        # parse file
        file_content = read_file(args.input_filename)
        parse_result = parser.parse(file_content)

        # generate file
        generator.generate(parse_result, args.output_filename)

if __name__ == "__main__":
    main()

# Doc2Source

Tool to convert from ANYTHING to ANYTHING. You can easily create your own parsers (using for example [pyparsing](http://pyparsing.wikispaces.com), [pandas](http://pandas.pydata.org), ....) and generators.

### Usage

```
usage: doc2source.py [-h] [--list-parsers] [--list-generators]
                     [parser_name] [generator_name] [input_filename]
                     [output_filename]

positional arguments:
  parser_name        name of parser
  generator_name     name of generator
  input_filename     name of file that needs to be parsed
  output_filename    name of output file (if supported by generator)

optional arguments:
  -h, --help         show this help message and exit
  --list-parsers     lists available parsers
  --list-generators  lists available generators
```

### Example: markdown structures to doctrine entities

```markdown

## Car 

* name (string)
* price (int)
* brand -> Brand

## Brand
* name (string)
```

Generate doctrine by executing following command

```bash
python doc2source.py dbdoc doctrine demo1.md
```

### Example: titanic data to JSON 

```
...
"Allison, Hudson Joshua Creighton"	1st	30	male	0
"Allison, Hudson JC (Bessie Waldo Daniels)"	1st	25	female	0
"Allison, Master Hudson Trevor"	1st	0.92	male	1
"Anderson, Harry"	1st	47	male	1
"Andrews, Kornelia Theodosia"	1st	63	female	1
...
```

Generate json by executing following command

```bash
python doc2source.py titanic titanic titanic.txt titanic.json
```

### Custom generators and parsers

Parsers are stored in **modules/parsers directory**. Generators in **modules/generators**.
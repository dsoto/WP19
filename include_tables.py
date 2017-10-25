# Tests the generation of a markdown syllabus with tables from supplemntary notebooks and a manuscript template.
#
# The tables are stored as files so that they can be tracked by a makefile.
#
# TODO: make a few tables and track dependencies in a makefile

# > python include_tables.py template.md output.md

import sys

template = sys.argv[1]
output = sys.argv[2]

import jinja2

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                                  # block_start_string='<<%',
                                  # block_end_string='%>>',
                                  comment_start_string='<!--',
                                  comment_end_string='-->')

template = template_env.get_template(template)
rendered = template.render()

# render template and output to file
with open(output, 'w') as f:
    f.write(rendered)





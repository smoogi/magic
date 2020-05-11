import sys
import re
import argparse

def extract_whitespaces(line, reverse=False):
    output = []
    if reverse:
	line = reversed(line)
        
    for character in line:
        if character in (' '):
            output.append(character)
        else:
            break

    return ''.join(output)

# Format option
format = r'^[^\s].+[^\s]$'
pre_wrap = '('
post_wrap = ')'

try:
    for line in sys.stdin:
        pre = extract_whitespaces(line)
        post = extract_whitespaces(line, reverse=True)
        line = line.rstrip().lstrip()
        text_object = re.search(format, line).group()
        output = '{}{}{}'.format(pre_wrap, text_object, post_wrap)
        if pre:
            output = pre + output
        if post:
            output = output + post
        sys.stdout.write(output+'\n')
except KeyboardInterrupt:
    sys.stdout.flush()
    pass

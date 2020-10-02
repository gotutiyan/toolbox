import argparse

def load_dict():
    char2es={}
    char2es["&"]="&amp;"
    char2es["'"]="&#x27;"
    char2es['`']="&#x60;"
    char2es['"']="&quot;"
    char2es['<']="&lt;"
    char2es['>']="&gt;"
    
    return char2es

def escape(line, char2es):
    escaped_line = ""
    for char in line:
        if char2es.get(char):
            escaped_line += char2es[char]
        else:
            escaped_line += char
    return escaped_line

def main(args):
    char2es = load_dict()
    escaped_lines = []
    with open(args.input) as fp:
        for line in fp:
            line = line.rstrip()
            escaped_lines.append(escape(line, char2es))
        
    if args.output:
        with open(args.output, 'w') as fp:
            for line in escaped_lines:
                fp.write(line + '\n')
    else:
        for line in escaped_lines:
            print(line)
    return


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',help='input file path', required=True)
    parser.add_argument('--output',help='output file path')

    return parser.parse_args()

if __name__=='__main__':
    args = get_parser()
    main(args)

    
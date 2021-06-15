import argparse
import re

def main(args):
    rows = open(args.input).read().split('\n')
    headers = []
    deep_appeared = {}
    for line in rows:
        if re.match(r"^#+", line) != None:
            headers.append(line)
            deep_appeared[line.split()[0]] = 1
    if args.output == None:
        args.output = '.'.join(args.input.split('.')[:-1]) + '.out.md'
    out_fp = open(args.output, "w")
    deep = -1
    prev_deep = -1
    for header in headers:
        n_deep = len(header.split()[0])
        if prev_deep < n_deep:
            deep += 1
        elif prev_deep > n_deep:
            deep -= 1
        if n_deep == 1:
            deep = 0
        prev_deep = deep
        out_fp.write("\t"*(deep) + "* ["+ ' '.join(header.split()[1:]) + "](" + header + ")\n")
    out_fp.write("\n")
    for row in rows:
        out_fp.write(row + "\n")
    
    out_fp.close()
    # print(headers)


    return


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output')
    

    return parser.parse_args()

if __name__=='__main__':
    args = get_parser()
    main(args)

    
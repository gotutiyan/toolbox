import argparse
import re

def main(args):
    rows = open(args.input).read().split('\n')
    headers = []
    sharp_appeared = {}
    for line in rows:
        if re.match(r"^#+", line) != None:
            headers.append(line)
            sharp_appeared[line.split()[0]] = 1
    sharp_list = list(sharp_appeared.keys())
    sharp_list.sort()
    sharp2deep = {}
    for i, sharp in enumerate(sharp_list):
        sharp2deep[sharp] = i
    print(sharp2deep)

    if args.output == None:
        args.output = '.'.join(args.input.split('.')[:-1]) + '.out.md'
    with open(args.output, "w") as out_fp:
        out_fp = open(args.output, "w")
        prev_deep = -1
        deep = -1
        for header in headers:
            sharp = header.split(' ')[0]
            if prev_deep < sharp2deep[sharp]:
                deep += 1
            elif prev_deep > sharp2deep[sharp]:
                deep = sharp2deep[sharp]
            prev_deep = deep
            out_fp.write("\t"*(deep) + "* ["+ ' '.join(header.split()[1:]) + "](" + header + ")\n")
        out_fp.write("\n")
        for row in rows:
            out_fp.write(row + "\n")
    return


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output')

    return parser.parse_args()

if __name__=='__main__':
    args = get_parser()
    main(args)

    
import argparse

def get_options():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", help = "input file like ***.csv",required=True)
    parser.add_argument('--output', help = "output file like ***.md")
    parser.add_argument('-c', '--center', help = 'center align', action = 'store_true')
    parser.add_argument('-r', '--right', help = 'right align', action = 'store_true')
    parser.add_argument('-l', '--left', help = 'left align (default)', action = 'store_true')

    return parser.parse_args()

def get_alignment(args):
    if args.center: return ':-:|'
    elif args.right: return '--:|'
    elif args.left: return ':--|'
    # default alignment
    return ':-:|'

def load_file(args):
    data = []
    number_of_row = 0
    with open(args.input) as fp:
        for line in fp:
            line = line.rstrip().split(',')
            data.append(line)
            number_of_row = max(number_of_row, len(line))
    return data, number_of_row

def process_data(args, data, number_of_row, alignment):
    buffer = []
    for i, line in enumerate(data):
        if i == 1:
            s = '|' + alignment * number_of_row 
            buffer.append(s)
        s = '|' + '|'.join(line) + '| '*(number_of_row - len(line)) + '|'
        buffer.append(s)
    return buffer
            
def main():
    args = get_options()
    alignment = get_alignment(args)
    data, number_of_row = load_file(args)
    buffer = process_data(args, data, number_of_row, alignment)
    if args.output:
        out = open(args.output, 'w')
        out.write('\n'.join(buffer))
        out.close()
    else :
        print('\n'.join(buffer))

if __name__ == "__main__":
    main()
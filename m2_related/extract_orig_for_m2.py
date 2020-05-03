import argparse

def main(args):
    out_file = open(args.out, 'w')
    with open(args.input) as fp:
        for line in fp:
            if line[0] == 'S':
                out_file.write(line[2:])
    out_file.close()
                

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", required=True)
    parser.add_argument("-out")
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_parser()
    main(args)
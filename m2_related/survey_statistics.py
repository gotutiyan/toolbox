import argparse
import statistics
import pandas as pd
import seaborn as sns
from collections import defaultdict
from matplotlib import pyplot as plt


def main(args):
    # out_file = open(args.out, 'w')
    stat = statistics.Statistics()
    edit_type2freq = defaultdict(int)
    edit_pos2freq = defaultdict(int)
    with open(args.input) as fp:
        for line in fp:
            if line[0] == 'S':
                stat.num_of_sents += 1
                # [2:] means to exclude 'S '
                sent = line[2:]
                stat.num_of_words += len(sent.split())
            elif line[0] == 'A':
                # [2:] means to exclude 'A '
                edit = line[2:].split('|||')
                # split begin index and end index
                edit[0] = edit[0].split()
                # example: 'R:BERV:SVA' -> ['R', 'BERV', 'SVA']
                edit[1] = edit[1].split(':')
                edit_type, edit_pos = edit[1][0], edit[1][1:]
                edit_type2freq[edit_type] += 1
                edit_pos2freq[':'.join(edit_pos)] += 1
    
    stat.show_stat()
    if args.error_pos:
        gen_figure(edit_pos2freq, 'freq', 'part of speech', path=args.error_pos)
    if args.error_type:
        gen_figure(edit_type2freq, 'freq', 'error_type', path=args.error_type)
                
        

def gen_figure(dict_obj, xlabel='x', ylabel='y', path='./'):
    sorted_dict = sorted(dict_obj.items(), key=lambda x:x[1], reverse=True)
    values = [elem[1] for elem in sorted_dict]
    keys = [elem[0] for elem in sorted_dict]
    df = pd.DataFrame({xlabel:values, ylabel:keys})
    sns.barplot(x=xlabel, y=ylabel, data=df)
    plt.savefig(path, format='png', dpi=300, bbox_inches='tight')
                

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", required=True)
    parser.add_argument("-out")
    parser.add_argument("-error_type")
    parser.add_argument("-error_pos")
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_parser()
    main(args)
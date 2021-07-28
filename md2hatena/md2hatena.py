'''
Convertor a format of mathmatics from markdown format to hatena-blog format.
$x_1$ → [tex:x_1]
'''
import argparse

def main():
    args = get_options()
    content = open(args.input, "r").read()
    content_hatena = convertor(content)
    output_file_name = '.'.join(args.input.split('.')[:-1]) + '_hatena.txt'
    write_content(content_hatena, output_file_name)
    return
    

def write_content(content_hatena, output_file_name):
    with open(output_file_name, "w") as fp:
        fp.write(content_hatena)
    return

def convertor(content):
    content_hatena = ""
    n_sysmbol = 0
    for char in content:
        if char == "$":
            if n_sysmbol % 2 == 0:
                content_hatena += "[tex:"
            else:
                content_hatena += "]"
            n_sysmbol += 1
        else:
            content_hatena += char
    content_hatena = content_hatena.replace('_', ' _ ')
    content_hatena = content_hatena.replace('^', '^ ')
    return content_hatena


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help = "input markdown file",required=True)
    return parser.parse_args()


    

if __name__ == "__main__":
    main()
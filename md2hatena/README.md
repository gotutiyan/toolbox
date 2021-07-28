# csv2md_table
This program converts CSV format data to markdown format data .

### Usage
`python csv2md_table.py --input <input_file_path> --output <output_file_path> [-h] [-c] [-r] [-l]`

`--input` is essential .
if you don't specific `--output`, output shows in your terminal .
`-h --help` : show help
`-c --center`: center alignmen . 
`-r --right`: right alignment .
`-l --left`: left alignment . (default)

### Demo
###### test.csv
~~~
,A,B,C
A,1,2,3
B,4,5,6
C,7,8,9
~~~

--->   `python3 csv2md_table.py -input test.csv -out out.txt` --->

###### out.txt
~~~
||A|B|C|
|:--|:--|:--|:--|
|A|1|2|3|
|B|4|5|6|
|C|7|8|9|
~~~

||A|B|C|
|:--|:--|:--|:--|
|A|1|2|3|
|B|4|5|6|
|C|7|8|9|

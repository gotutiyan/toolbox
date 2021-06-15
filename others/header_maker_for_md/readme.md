# Header Maker for MD

Code for making headers for a markdown document.

# Usage

`python3 header_maker_for_md.py --input <input file path> --ouput <output file path> `

`--input` is must be specified.

`--output` is optional. If you do not specify, the output file name is `<input_file_name>.out.md`

# Demo

```
python3 header_marker_for_md.py --input demo/sample_input.md --out demo/sample_out.md
```

* demo/sample_input.md

  ```md
  # 1
  This is a sample sentence.
  
  ### 2
  This is a sample sentence.
  
  #### 3
  This is a sample sentence.
  
  ##### 4
  This is a sample sentence.
  
  ### 5
  This is a sample sentence.
  
  ##### 6
  This is a sample sentence.
  
  # 7
  This is a sample sentence.
  ```

* demo/sample_out.md

  ```
  * [1](# 1)
  	* [2](### 2)
  		* [3](#### 3)
  			* [4](##### 4)
  	* [5](### 5)
  		* [6](##### 6)
  * [7](# 7)
  
  # 1
  This is a sample sentence.
  
  ### 2
  This is a sample sentence.
  
  #### 3
  This is a sample sentence.
  
  ##### 4
  This is a sample sentence.
  
  ### 5
  This is a sample sentence.
  
  ##### 6
  This is a sample sentence.
  
  # 7
  This is a sample sentence.
  ```
  
  

# Header Maker for MD

Code for making headers for markdown document.

# Usage

`python3 header_maker_for_md.py --input <input file path> --ouput <output file path> `

`--input` is must be specified.

`--output` is optional. If you do not specify, the output file name is `<input_file_name>.out.md`

# Demo

```
python3 python3 header_marker_for_md.py --input demo/sample_input.md --out demo/sample_out.md
```

* demo/sample_input.md

  ```md
  # This
  
  ### is
  
  ##### demo
  
  # This
  
  ## is
  
  ### also
  
  #### demo
  
  ```

* sample_out.md

  ```
  * [This](# This)
    * [is](### is)
      * [demo](##### demo)
  * [This](# This)
    * [is](## is)
      * [also](### also)
        * [demo](#### demo)
  
  # This
  
  ### is
  
  ##### demo
  
  # This
  
  ## is
  
  ### also
  
  #### demo
  
  ```

  

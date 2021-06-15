# Header_maker_for_md

### Usage

I assumed you execute this code in this directory.

```
python3 python3 ../header_marker_for_md.py --input sample_input.md --out sample_out.md
```

* sample_input.md

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

  

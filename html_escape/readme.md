# html escape

The program to escape the input.

# Usage

`python3 html_escape.py --input <input file path> --ouput <output file path> `

`--input` is must be specified.

If you don't specfy `--output`, outputs shows in your terminal.

# Demo

* demo/input.txt

```txt
<html>
  <a href="sample_url.com">google</a>
</html>
```

Running program

`python3 html_espcape --input demo/input.txt --output demo/output.txt`

* demo/output.txt

```
&lt;html&gt;
  &lt;a href=&quot;sample_url.com&quot;&gt;google&lt;/a&gt;
&lt;/html&gt;
```


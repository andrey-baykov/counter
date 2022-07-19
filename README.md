# Counter framework for CLI
The application takes a string throw command line interface and returns the number of unique characters in the string.
Since first use the application caches the results and when the method is given a string previously encountered, it will simply retrieve the stored result.
___

## Parameters:

**--string**
> Provide string


**--file**
> Provide path to file with text


## Priority
If the application was taken both parameters then parameter `--file` has higher priority. Parameter `--string` will be ignored.

## Examples

```commandline
% python3 src/counter/collect_framework.py --string Hello --file textfile.txt
% python3 src/counter/collect_framework.py --file textfile.txt
% python3 src/counter/collect_framework.py --string Hello
```
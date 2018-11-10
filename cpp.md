1) Shows all predefined macros
```bash
touch foo.h; cpp -dM foo.h
```
2) Remove linemarkers from the output of the preprocessor. 
Can be useful when you use cpp on something that is not c code.
```bash
gcc -E -P
```
3) Show default search paths for #include <...>
```bash
cpp -v /dev/null -o /dev/null
```

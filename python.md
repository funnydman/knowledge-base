Invoke function from shared c library:
```python3
import ctypes

testlib = ctypes.CDLL('/path/to/libtest.so')
print(testlib.<name_of_func>(15))
```

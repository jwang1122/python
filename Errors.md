# Python Errors

## Machine Learning
```
Python: 3.6.11 (default, Jun 29 2020, 13:22:26) 
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
scipy: 1.5.2
numpy: 1.19.1
matplotlib: 3.3.0
pandas: 1.1.0
sklearn: 0.23.2
```

* Runtime Error
```
RuntimeError: The current Numpy installation ('c:\\Users\\12818\\workspace\\python-I\\env\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
```
* Caused: 
Failed Version | Success Version |
|--- |--- |
matplotlib-3.3.3 | matplotlib-3.3.0
numpy-1.19.4     | numpy-1.19.3

* Solution
```
pip install numpy==1.19.3
pip install matplotlib==3.3.0

```

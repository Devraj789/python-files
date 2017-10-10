Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> pi
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> math.pi
3.141592653589793
>>> print('the value of pi is: ',math.pi)
the value of pi is:  3.141592653589793
>>> math.sqrt(8)
2.8284271247461903
>>> math.sqrt(4)
2.0
>>> math.sin(45)
0.8509035245341184
>>> math.sin(30)
-0.9880316240928618
>>> r = 5
>>> print("area of circle is: ",math.pi*r*r)
area of circle is:  78.53981633974483
>>> print("perimeter of circle is: ",2*math.pi*r)
perimeter of circle is:  31.41592653589793
>>> p = 'Dharan'
>>> dir(p)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> p = 'kathmandu'
>>> dir(p)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> p[3]
'h'
>>> p[-1]
'u'
>>> p[1,3]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    p[1,3]
TypeError: string indices must be integers
>>> p[1:4]
'ath'
>>> p[1:5]
'athm'
>>> p[:]
'kathmandu'
>>> p[:4]
'kath'
>>> p[1:]
'athmandu'
>>> s = 'abcd'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s.index('d')
3
>>> s.upper()
'ABCD'
>>> s.lower()
'abcd'
>>> s.find('d')
3
>>> s.find('b')
1
>>> s.islower90
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s.islower90
AttributeError: 'str' object has no attribute 'islower90'
>>> s.lower()
'abcd'
>>> b = s.upper()
>>> b.islower()
False
>>> len(s)
4
>>> s = abc d
SyntaxError: invalid syntax
>>> s = 'abc d'
>>> len(s)
5
>>> n = '1'
>>> type(n)
<class 'str'>
>>> a = 'hello'
>>> b = 'world'
>>> a+b
'helloworld'
>>> a = 2
>>> float(a)
2.0
>>> b = 4.5
>>> int(b)
4
>>> str(a)
'2'
>>> str('b')
'b'
>>> str(b)
'4.5'
>>> c = 'abc'
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'abc'
>>> c = '1'
>>> int(c)
1
>>> a = '1'
>>> b = '2'
>>> int(a) + int(b)
3
>>> s = 'Ram has 2 apple and 3 orange'
>>> int(apple)+int(orange)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(apple)+int(orange)
NameError: name 'apple' is not defined
>>> s = 'ram has 2 apple and 3 orange'
>>> len(8)+len(20)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    len(8)+len(20)
TypeError: object of type 'int' has no len()
>>> len(8)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    len(8)
TypeError: object of type 'int' has no len()
>>> s.find('2')
8
>>> s.find('3')
20
>>> int(s[8]) + int(s[16])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(s[8]) + int(s[16])
ValueError: invalid literal for int() with base 10: 'a'
>>> a = 'abc'
>>> a.zfill(10)
'0000000abc'
>>> bin(8)
'0b1000'
>>> bin(8)
'0b1000'
>>> bin(8).zfill(16)
'00000000000b1000'
>>>  a = 8
 
SyntaxError: unexpected indent
>>> a = 8
>>> bin(8)
'0b1000'
>>> a [2:]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a [2:]
TypeError: 'int' object is not subscriptable
>>> a = bin(8)
>>> a
'0b1000'
>>> b=a[2:]
>>> b
'1000'
>>> b.zfill(16)
'0000000000001000'
>>> a = 'abc'
>>>  b = 'h'
 
SyntaxError: unexpected indent
>>> b = 'h'
>>> b * 3
'hhh'
>>> a *10
'abcabcabcabcabcabcabcabcabcabc'
>>> list
<class 'list'>
>>> L = ['a' , -5 , 5.0 , 10]
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> L[2]
5.0
>>> L[:3]
['a', -5, 5.0]
>>> l = [2,3]
>>> m = [5,6]
>>> l+m
[2, 3, 5, 6]
>>> l*2
[2, 3, 2, 3]
>>> l.index['a']
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    l.index['a']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> L.index['a']
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    L.index['a']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> L.index['2']
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    L.index['2']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> L.index[2]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    L.index[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a = ['a', 'b']
>>> a.index['a']
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.index['a']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a= [10 , 20 ,30 ,40 ,'abc']
>>> a.pop()
'abc'
>>> print a
SyntaxError: Missing parentheses in call to 'print'
>>> print(a)
[10, 20, 30, 40]
>>> a.remove(40)
>>> print(a)
[10, 20, 30]
>>> a.add(100)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.add(100)
AttributeError: 'list' object has no attribute 'add'
>>> a.insert(20)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.insert(20)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> a.insert(50)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.insert(50)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> a = 'String'
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> a.reverse(a)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.reverse(a)
AttributeError: 'str' object has no attribute 'reverse'
>>> a.reverse('a')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.reverse('a')
AttributeError: 'str' object has no attribute 'reverse'
>>> 

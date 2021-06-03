*Python3, Tip~*
======  

*01. Functions_dir()*
------  
> 모듈의 모든 정보를 가져와라.  
> 실행  
``` python
print(dir())
```  
> 결과  
```python
['__loader__', '__name__','__spec__', ...]
```  

*02. Value__all__특수 변수*
------  
> file __init__.py  
``` python  
__all__ = ['circle','PI']

PI = 3.14


def circle(value):
~ 내용


def square(value):
~ 내용
```  

> file run.py 실행  
``` python  
# shapes = package, area = module
from shapes.area import *

print(dir())
```  
> 결과  
``` python
['__loader__', '__name__','__spec__', ..., circle, PI]
```

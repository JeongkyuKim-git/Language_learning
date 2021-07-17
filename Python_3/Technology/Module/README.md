*스크립트 vs 모듈*
========  

*스크립트*
------  
> 프로그램을 작동시키는 코드를 담은 실행 용도의 파일  

*모듈*
------  
> 프로그램에 필요한 변수들이나 함수들을 정의해 놓은 파일  

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

모듈 (Module)
=============
> 여러 파일에 대해 하나의 기능을 하는 파일을 모듈이라고 한다.  
> 장점: 코드를 재사용 할 수 있다.
> 기능: 01. 모듈을 만드는 방법과 02. 불러오는 방법  

<img src="https://user-images.githubusercontent.com/66001539/119265203-d1d05980-bc20-11eb-820b-9c211d1f3690.png" width="600px" height="300px" title="px(픽셀) 크기 설정" alt="Image_machine"></img><br/>  

> Example) area.py 모듈이 존재할 경우  
> 함수가 2개 존재한다고 했을 때,
``` python
def circle(radius):
    return 3.14 * radius * radius

def square(length):
    return length * length
```  
> run.py라는 main 파일에서 import area는 두개의 함수를 사용할 수 있다.  
> 하지만 함수가 엄청 많을 경우 불필요한 import가 될 수 있기 때문에 from을 사용할 수 있다.  
> from area import circle  
``` python
# 모듈의 전체 함수 불러오기
import area

# 모듈의 각 함수 불러오기
from area import circle

# 모듈의 사용할 여러개 함수 불러오기
from area import circle, square, [...]

# 모듈의 사용할 모든 함수 불러오기
from area import *
```  
> 모듈의 이름을 유사하게 사용할 경우 간단하게 별칭을 이용하여, 사용하는 방법  
```python
import area as ar
ar. ~
```  


Package
=============
> 모듈(Module)  

<img src="https://user-images.githubusercontent.com/66001539/120498056-e5867780-c3f9-11eb-9dd8-9660b0d3f083.png" width="600px" height="300px" title="px(픽셀) 크기 설정" alt="Image_machine"></img><br/>  
*모듈과 패키지*
-------------  
> 패키지를 어떻게 만들고 사용하는지 이해하는 방법  

<img src="https://user-images.githubusercontent.com/66001539/120498641-56c62a80-c3fa-11eb-9885-5b8ebcdf7ff8.png" width="600px" height="300px" title="px(픽셀) 크기 설정" alt="Image_machine"></img><br/>  

*01. import 방식*
-------------  
> 그냥 import 뒤에 가져오고 싶은 모듈이나 패키지를 써 주면 됩니다. 하지만 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없습니다.  
``` python  
# 패키지 임포트
import mymath

# 서브패키지 임포트
import mymath.shapes

# 모듈 임포트
import mymath.shapes.area

# 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없음 
import mymath.shapes.area.circle # 오류
```  

*02. from 방식*
-------------   
> from 뒤에는 모듈이나 패키지가 올 수 있습니다. import 뒤에는 모듈이나 패키지 안에서 가져오고 싶은 걸 써 줍니다. import 뒤에는 . 을 쓸 수 없습니다.  
``` python  
# 패키지 안에 있는 패키지 임포트
from mymath import shapes

# 패키지 안에 있는 모듈 임포트
from mymath.shapes import area

# 모듈 안에 있는 함수 임포트
from mymath.shapes.area import circle

# import 뒤에는 . 을 쓸 수 없음 
from mymath import shapes.area # 오류
```  

*03. 상대, 절대 경로*
-------------  
> 현재 경로에서 임포트하는 방법
``` python  
# 절대 경로 임포트
from mymath.shapes import area, volume

# 상대 경로 임포트
from . import area, volume
```  

*04. 상대, 절대 경로*
-------------  
> 다른 패키지 경로에서 임포트하는 방법
``` python  
# 절대 경로 임포트
from mymath.stats.average import data_mean

# 상대 경로 임포트
from ..stats.average import data_mean
```  

[Top Button](#)

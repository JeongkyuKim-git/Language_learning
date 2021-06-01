유용한 스탠다드 모듀들
=============
> 모듈들에 대한 자세한 정보는 파이썬 공식 문서에서 찾을 수 있습니다:  
[참조 내용-Standard_module_URL](https://docs.python.org/ko/3/library/)  
  
*math (수학 모듈)*
-------------  
>   math는 기본적인 수학 모듈입니다. 여러 수학적인 함수를 제공해 줍니다.  
```python
import math

# 코사인 함수 (모든 삼각함수는 라디안을 사용합니다)
print(math.cos(0))

# 로그 함수
print(math.log10(100))
```  
  
``` python
1.0
2.0
```  

*random (난수 모듈)*
-------------  
> random 모듈은 랜덤 한 숫자를 생성하기 위한 다양한 함수들을 제공해 줍니다.  
```python
import random

# 랜덤한 정수 1 <= N <= 20 
print(random.randint(1, 20))

# 랜덤한 소수 0 <= x <= 1
print(random.uniform(0, 1))
```    

``` python
3
0.599056286966887
```  

*datetime (날짜, 시간 모듈)*
-------------  
> datetime 모듈은 날짜와 시간을 다루기 위한 다양한 '클래스'를 갖추고 있습니다. 
```python
import datetime 

# 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)
```  
``` python
2020-08-26 14:09:36.361025
Wednesday, August 26th 2020
2020-03-14 13:06:15
165 days, 1:03:21.361025
```  

*os (날짜, 시간 모듈)*
-------------  
>   OS는 Operating System, 즉 운영체제의 약자입니다. os 모듈을 통해서 파이썬으로 운영체제를 조작하거나 운영체제에 대한 정보를 가져올 수 있습니다.
```python
import os

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인 
print(os.getcwd())

# 현재 프로세스 ID 확인 
print(os.getpid())
```  

```python
codeit
/Users/codeit/PycharmProjects/standard_modules
2346
```  

*os.path (경로 탐색)*
-------------  
>   os.path 모듈은 파일 경로를 다룰 때 쓰입니다.  
```python
import os.path

# 프로젝트 디렉토리 경로 '/Users/codeit/PycharmProjects/standard_modules'
# 현재 파일 경로 '/Users/codeit/PycharmProjects/standard_modules/main.py'

# 주어진 경로를 절대 경로로
print(os.path.abspath('..'))

# 주어진 경로를 현재 디렉토리를 기준으로 한 상대 경로로
print(os.path.relpath('/Users/codeit/PycharmProjects'))

# 주어진 경로들을 병합
print(os.path.join('/Users/codeit/PycharmProjects', 'standard_modules'))
```  
```python
/Users/codeit/PycharmProjects
..
/Users/codeit/PycharmProjects/standard_modules
```  

*re (날짜, 시간 모듈)*
-------------  
> 프로그래밍에서 Regular Expression (RegEx, re, 한국어로는 정규 표현식)은 특정한 규칙/패턴을 가진 문자열을 표현하는 데 사용됩니다.  

```python
import re 

# 알파벳으로 구성된 단어들만 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))
```  
```python
<re.Match object; span=(0, 1), match='I'>
<re.Match object; span=(0, 4), match='love'>
None

None
None
<re.Match object; span=(0, 7), match='python3'>
```  

*pickle (날짜, 시간 모듈)*
-------------  
> pickle 을 사용하면 파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장할 수 있고 저장된 오브젝트를 읽어올 수도 있습니다.   
```python
import pickle

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}  

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

# filename.pickle에 있는 오브젝트를 읽어옴 
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)
```  
``` python
{'my': 'dictionary'}
```  

*json (날짜, 시간 모듈)*
-------------  
>   
```python

```  


*copy (날짜, 시간 모듈)*
-------------  
>   
```python

```  


*sqlite3 (날짜, 시간 모듈)*
-------------  
>   
```python

```  
 

[Top Button](#)

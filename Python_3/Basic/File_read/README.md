File_read
=============
> file open (line)  

*Read line?*
-------------
encoding = 'UTF8' --> 한글 사용

``` python
with open('Data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())  
```

>  print(line.strip())
>  print(line)
>  두개의 차이는 출력되는 문장의 화이트 스페이스 때문이다. (" ", "\t", "\n")
    
[Top Button](#)

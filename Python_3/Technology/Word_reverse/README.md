*단어를 거꾸로 변경하는 방법*
======  
> Example)  

```Python
word = "토마토"
print(word)
```  
> 토마토

```Python
word_reverse = "토마토"
word_reverse.reverse()
print(word_reverse)
```  
> 토마토  

<br>

***

> 실험 결과  
  
| Algorithm | 	TimeIt Execution Time (Best of 5) | Slowness |
| ---------- | :--------- | :----------: |
| Slicing    | 	0.449 usec       | 	1x       |
| List reverse()    | 2.46 usec       | 5.48x     |
| reversed() + join()    | 2.49 usec       | 5.55x       |
| for loop	    | 5.5 usec       | 12.25x       |
| while loop    | 9.4 usec       | 20.94x       |
| Recursion    | 24.3 usec       | 54.12x       |
  

파이썬은 `데코레이터(decorator)`라는 기능을 제공한다.  
데코레이터는 장식하다, 꾸미다라는 뜻의 decorate에 er(or)을 붙인 말인데 장식하는 도구 정도로 설명할 수 있다.

즉, `함수(메서드)를 장식한다`고 해서 이런 이름이 붙었다. 

``` python
class Calc:
    @staticmethod    # 데코레이터
    def add(a, b):
        print(a + b)
```

이번 장에서는 데코레이터를 만들고 사용하는 방법을 알아보겠다. 

출처 : https://dojang.io/mod/page/view.php?id=2427
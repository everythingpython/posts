from typing import Union

def func1(a: Union[int,float], b: Union[int,float]) ->  Union[int,float]:
    return a+b

def func2(a: int|float, b:int|float) ->  int|float:
    return a+b






func1("abhi", "ram")
func2("abhi", "ram")
func1(1, 5)
func2(10.0, 2)
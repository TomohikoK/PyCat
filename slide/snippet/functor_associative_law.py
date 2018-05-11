from typing import List, TypeVar

T = TypeVar('T')

def func1(arg: T) -> List[T]: return [arg]

def func2(arg: T) -> List[T]: return [arg, arg]

def func3(arg: T) -> List[T]: return [arg, arg, arg]

x: int = 42
assert (lambda x: func3(func2(x)))(func1(x)) \
    == func3(func2(func1(x)))

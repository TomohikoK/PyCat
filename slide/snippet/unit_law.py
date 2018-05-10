from typing import TypeVar, List

T = TypeVar('T')

x: int = 1

def func(arg: T) -> List[T]:
    return [arg, arg, arg]

assert flatten(unit(func(x))) == func(x)
assert func(x) == flatten(func(unit(x)))

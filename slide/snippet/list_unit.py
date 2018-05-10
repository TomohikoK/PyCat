from typing import List, TypeVar

T = TypeVar('T')

def unit(arg: T) -> List[T]:
    return [arg]

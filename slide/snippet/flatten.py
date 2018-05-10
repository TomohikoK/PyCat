from typing import List, TypeVar

T = TypeVar('T')

def flatten(arg: List[List[T]]) -> List[T]:
    result = []
    for inner in arg:
        result.extend(inner)
    return result

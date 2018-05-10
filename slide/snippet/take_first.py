from typing import List, Optional, TypeVar

T = TypeVar('T')

def take_first(arg: List[T]) -> Optional[T]:
    if len(arg):
        return arg[0]
    else:
        return None

from typing import List

def length_of_string(arg: str) -> int:
    return len(arg)

x: List[str] = ['a', 'bb', 'ccc']
y: List[int] = list(map(length_of_string, x))
assert y == [1, 2, 3]

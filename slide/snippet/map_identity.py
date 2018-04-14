from typing import List

x: List[str] = ['a', 'b']
assert x == list(map(identity, x))

from typing import TypeVar

A = TypeVar('A')  # 型変数

def id(arg: A) -> A:
    return arg

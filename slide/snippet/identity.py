from typing import TypeVar

A = TypeVar('A')  # 型変数

def identity(arg: A) -> A:
    return arg

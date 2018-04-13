import typing

A = typing.TypeVar('A')  # 型変数

def id(arg: A) -> A:
    return arg

from typing Callable

def func(arg: int) -> str:
    return str(arg)

func: Callable[[int], str]  # 関数宣言以外での表記

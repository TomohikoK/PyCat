def double(arg: int) -> int:
    return arg * 2

x: List[str] = ['a', 'bb']
x1 = list(map(double @ length_of_str, x))
x2 = list(map(double, list(map(length_of_str, x))))

assert x1 == x2  # どちらの値も[2, 4]
